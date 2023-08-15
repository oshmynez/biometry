from gateway.db import Clients
from gateway.models import ClientAuth
from gateway.session import close_db, get_db


class ClientDataValidator:
    def validate_data(self, client: ClientAuth):
        try:
            session = get_db()
            if session:
                res = session.query(Clients).filter(Clients.email == client.email, Clients.password == client.password).all()
                if res:
                    return res[0]
                return []
        except Exception as ex:
            return []
        finally:
            close_db(session)


def authenticate_user(client: ClientAuth) -> ClientDataValidator:
    return ClientDataValidator()
