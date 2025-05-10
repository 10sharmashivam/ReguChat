# ReguChat
Built an autonomous AI agent for regulated industries using BERT-based LLMs and RAG, achieving 90% compliant response accuracy. Developed Flask APIs for real-time queries and a React dashboard for monitoring, deployed on GCP with Docker.

An open-source AI agent for compliant enterprise conversations, built for Eloquent AI’s use case. Uses BERT-based LLMs, RAG, Flask APIs, and GCP deployment.

## Setup
1. Clone: `git clone https://github.com/10sharmashivam/ReguChat.git`
2. Install: `pip install -r requirements.txt`
3. Install spaCy model: `python -m spacy download en_core_web_sm`
4. Run: `python main.py`

## Tech Stack
- AI: HuggingFace (BERT), RAG (FAISS)
- Backend: Flask, PostgreSQL
- Deployment: GCP Cloud Run, Docker