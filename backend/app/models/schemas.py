from pydantic import BaseModel

class DetectionResult(BaseModel):
    label: str
    box: list[int]
