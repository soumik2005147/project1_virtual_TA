# project1_virtual_TA

 For the *Tools in Data Science* (TDS) course at IIT Madras. This FastAPI‑based service backs a Retrieval‑Augmented Generation (RAG) pipeline, letting students ask questions (including screenshots) and receive context‑aware answers with source links from course discussion forums and documentation.



## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/soumik2005147/project1_virtual_TA.git
cd project1_virtual_TA
```

### 2. Setup Python virtual environment

```bash
python3 -m venv venv
# Windows\ .\venv\Scripts\activate
# macOS/Linux\ source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment variables

Create a `.env` in the project root with:

```
OPENAI_API_KEY=<your-openai-or-proxy-key>
```

### 5. Prepare the knowledge base

If you've already scraped and built `knowledge_base.db`, skip this step. Otherwise:

```bash
python preprocess.py       # downloads/discourse & markdown chunks
python embed_chunks.py     # computes embeddings and saves to DB
```

### 6. Run locally

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

* Query endpoint: `POST http://localhost:8000/query`
* Health check: `GET  http://localhost:8000/health`

## 📦 Deployment on Render.com

1. Push to GitHub.
2. Create a new Web Service in Render:

   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   * **Env Var**: `OPENAI_API_KEY` (link to your secret)
3. Deploy—your Virtual TA will be live.


## 📜 License

MIT © IIT Madras
