from fastapi import FastAPI

app = FastAPI(
    title="Order Assignment System",
    description="High-performance delivery order assignment backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Order Assignment System Backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }