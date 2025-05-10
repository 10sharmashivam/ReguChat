from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

class LLM:
    def __init__(self, model_name="bert-base-uncased"):
        """
        Initialize the LLM.

        Args:
            model_name (str): The name of the HuggingFace model to use. Defaults to "bert-base-uncased".

        Returns:
            None
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def predict(self, text):
        """
        Make a prediction on a given text using the fine-tuned BERT model.

        Args:
            text (str): The text to make a prediction on.

        Returns:
            list: A list of the predicted probabilities for each class, where the index in the list corresponds to the class index in the model's config.
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)
        return torch.softmax(outputs.logits, dim=1).tolist()[0]