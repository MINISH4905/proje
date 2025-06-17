from fastapi import APIRouter, UploadFile, File
from app.services.object_detector import detect_objects

router = APIRouter()

@router.post("/detect")
async def detect_objects_route(file: UploadFile = File(...)):
    image = await file.read()
    result = detect_objects(image)
    return {"objects_detected": result}
