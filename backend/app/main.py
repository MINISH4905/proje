from fastapi import FastAPI
from app.routes import face, object
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(face.router, prefix="/face")
app.include_router(object.router, prefix="/object")
