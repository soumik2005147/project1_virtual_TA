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

@app.api_route("/", methods=["GET", "POST"])
async def root(request: Request):
    """
    Respond to both GET and POST at "/".
    If it’s a POST, the body is ignored and we return the same message.
    """
    return {"message": "Hello from Virtual TA!"}
