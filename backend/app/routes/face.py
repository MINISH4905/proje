from fastapi import APIRouter, UploadFile, File
from app.services.face_recognizer import detect_face

router = APIRouter()

@router.post("/detect")
async def detect_faces(file: UploadFile = File(...)):
    image = await file.read()
    result = detect_face(image)
    return {"faces_detected": result}
