# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ─── CORS CONFIGURATION ────────────────────────────────────────────────────────
# Allow all origins (you can narrow this later if you prefer):
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # <-- allow requests from any origin
    allow_methods=["*"],      # <-- allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],      # <-- allow any headers
)
# ────────────────────────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    return {"message": "Hello from Virtual TA!"}
