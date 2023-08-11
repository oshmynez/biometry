from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from pydantic import BaseModel

from gateway.db import get_db, close_db
from gateway.models import Clients

app = FastAPI()


class Client(BaseModel):
    id: str
    email: str
    password: str
    identification_number: str


class ClientDataValidator:
    def validate_data(self, client: Client):
        try:
            session = get_db()
            if session:
                res = session.query(Clients).filter(Clients.email == client.email, Clients.password == client.password).all()
                if res:
                    return True
        except:
            return False
        finally:
            close_db(session)


def authenticate_user(client: Client) -> ClientDataValidator:
    return ClientDataValidator()


@app.post("/authentication")
def authentication(client: Client, validator: ClientDataValidator  = Depends(authenticate_user)):
    if validator.validate_data(client):
        return {"message": "Data is valid"}
    else:
        raise HTTPException(status_code=400, detail="Invalid data")


@app.post("/create")
def create_data(client: Client, validator: ClientDataValidator  = Depends(authenticate_user)):
    try:
        if validator.validate_data(client):
            session = get_db()
            client = Clients(first_name=client['first_name'], email=client['email'],
                             password=client['password'], identification_number=client['identification_number'])
            session.add(client)
            return {"message": "Client is created"}
        return {"message": "Client is not created"}
    except:
        raise HTTPException(status_code=500, detail="Error of creating client")
    finally:
        close_db(session)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
