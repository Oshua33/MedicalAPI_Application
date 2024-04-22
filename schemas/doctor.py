from pydantic import BaseModel


class DoctorData(BaseModel):
    username: str
    specialization: str
    phone: str
    is_available: bool = True



    class Config:
        json_schema_extra = {
            "example": {
                "username": "Dr Onome",
                "specialization": "Pediatrician",
                "phone": "+2349076543210",
                "is_available": True,
                "password": "dronome"
            }
        }


class DoctorCreate(DoctorData):
    password: str

class Doctor(DoctorData):
    id: int

doctors: list[Doctor] = []
