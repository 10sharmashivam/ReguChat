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

## Project Structure

```
ReguChat/
├── api/                    # Flask backend and API logic
│   ├── routes.py           # API endpoints (e.g., /query, /monitor)
│   ├── models.py           # Database models (PostgreSQL for RAG context)
│   └── utils.py            # Helper functions (e.g., response formatting)
├── ai/                     # AI and LLM logic
│   ├── llm.py              # BERT model loading, fine-tuning, inference
│   ├── rag.py              # RAG pipeline (FAISS vector search)
│   ├── compliance.py       # Compliance rules (e.g., keyword filtering)
│   └── data/               # Sample datasets (e.g., customer queries)
│       ├── queries.json    # Sample queries for testing
│       └── compliance_rules.json  # Compliance keywords/rules
├── frontend/               # Optional React dashboard (for Full-Stack JD)
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── QueryMonitor.js # Dashboard for query/response visualization
│   │   └── Chart.js        # Chart.js for metrics
│   ├── package.json        # Node.js dependencies
│   └── public/             # Static assets
├── deployment/             # Deployment and CI/CD configs
│   ├── Dockerfile          # Docker configuration
│   ├── kubernetes.yaml     # Kubernetes deployment manifest
│   └── .github/workflows/  # GitHub Actions CI/CD pipeline
│       └── deploy.yml      # CI/CD for GCP Cloud Run
├── tests/                  # Unit tests
│   ├── test_llm.py         # Tests for LLM inference
│   ├── test_rag.py         # Tests for RAG pipeline
│   └── test_api.py         # Tests for Flask APIs
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (e.g., GCP credentials)
├── README.md               # Project overview, setup, usage
└── main.py                 # Entry point for Flask app

```