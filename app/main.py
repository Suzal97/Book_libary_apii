# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import book
from app.core.config import settings
from app.database import client

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(book.router, prefix="/books", tags=["books"])

# Close MongoDB connection on shutdown
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
