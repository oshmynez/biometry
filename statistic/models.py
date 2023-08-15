from pydantic import BaseModel


class Transaction(BaseModel):
    id: str
    email: str
    password: str
    identification_number: str
