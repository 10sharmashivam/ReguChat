import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel

class RAG:
    def __init__(self):
        """
        Initialize the RAG model.

        This creates a BERT model and tokenizer, a FAISS index for efficient nearest neighbor search,
        and an empty list to store the input contexts.

        :return: None
        """
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModel.from_pretrained("bert-base-uncased")
        self.index = faiss.IndexFlatL2(768)  # BERT embedding size
        self.contexts = []

    def add_context(self, texts):
        
        """
        Add one or more input contexts to the RAG model.

        Each context is converted to a BERT embedding, and then added to the FAISS index and the list of stored contexts.

        :param texts: one or more string contexts to add to the model
        :return: None
        """
        embeddings = []
        for text in texts:
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
            embedding = self.model(**inputs).last_hidden_state.mean(dim=1).detach().numpy()
            embeddings.append(embedding)
        embeddings = np.vstack(embeddings)
        self.index.add(embeddings)
        self.contexts.extend(texts)

    def query(self, text, k=1):
        """
        Query the RAG model for the k most similar contexts.

        This first converts the input text to a BERT embedding, then uses the FAISS index to find the k nearest neighbors in the stored contexts.

        :param text: the text to query the model with
        :param k: the number of nearest neighbors to return (default 1)
        :return: a list of the k most similar contexts
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        embedding = self.model(**inputs).last_hidden_state.mean(dim=1).detach().numpy()
        distances, indices = self.index.search(embedding, k)
        return [self.contexts[i] for i in indices[0]]