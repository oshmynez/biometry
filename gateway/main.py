import uvicorn
from fastapi import Depends, FastAPI, HTTPException

from gateway.bl import ClientDataValidator, authenticate_user
from gateway.db import Clients
from gateway.models import Client, ClientAuth, ClientResponse
from gateway.session import close_db, get_db

app = FastAPI()


@app.post("/authentication")
def authentication(client: ClientAuth, validator: ClientDataValidator = Depends(authenticate_user)):
    try:
        result = validator.validate_data(client)
        if len(result) > 0:
            return ClientResponse(first_name=result.first_name, email=result.email, code=200, message='client is authenticated')
        else:
            return ClientResponse(status_code=400, message='client doesn\'t exist with this email and password')
    except Exception:
        raise HTTPException(status_code=500, detail={'message': "Internal Server Error"})


@app.post("/create")
def create_data(client: Client, validator: ClientDataValidator = Depends(authenticate_user)):
    try:
        result = validator.validate_data(ClientAuth(email=client.email, password=client.password))
        if len(result) > 0:
            session = get_db()
            client = Clients(first_name=client['first_name'], email=client['email'],
                             password=client['password'], identification_number=client['identification_number'])
            session.add(client)
            return ClientResponse(first_name=client.first_name, email=client.email, code=201, message='client is created')
        return ClientResponse(code=200, message='client is\'t created')
    except:
        raise HTTPException(status_code=500, detail="Error of creating client")
    finally:
        close_db(session)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
