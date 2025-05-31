# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ─── CORS CONFIGURATION ────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# ────────────────────────────────────────────────────────────────────────────────

@app.api_route("/", methods=["GET", "POST", "HEAD"])
async def root(request: Request):
    return {"answer": "Hello from Virtual TA!"}
