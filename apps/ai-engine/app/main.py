from fastapi import FastAPI

app = FastAPI(title="SEO AI Engine")

@app.get("/health")
def health():
    return {"status": "AI Engine Running"}
