# Application Entry Point
from app.app import app
import uvicorn

if __name__ == "__main__":
    # ASGI Web Server
    uvicorn.run(
        "app.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )