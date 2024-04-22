from pydantic import BaseModel



class PatientData(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int
    sex: str
    weight: float
    height: float
    phone_number: str


class PatientCreate(PatientData):
    password: str


    class Config:
        json_schema_extra = {
            "example": {
                "username": "bleBle",
                "first_name": "blessed",
                "last_name": "bello", 
                "age": 28,
                "sex": "male",
                "weight": 61,
                "height": 5.4,
                "phone_number": "+2348088676895",
                "password": "blessed123"
            }
        }

class Patient(PatientCreate):
    id: int



patients: list[Patient] = []
