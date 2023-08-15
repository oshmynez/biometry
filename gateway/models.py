from typing import Optional

from pydantic import BaseModel


class ClientBaseModel(BaseModel):
    pass


class Client(ClientBaseModel):
    id: str
    first_name: str
    email: str
    password: str
    identification_number: str


class ClientAuth(ClientBaseModel):
    email: str
    password: str


class ClientResponse(ClientBaseModel):
    first_name: Optional[str] = None
    email: Optional[str] = None
    status_code: int
    message: str
