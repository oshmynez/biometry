from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from concurrent import futures
import grpc
import time

import common.transaction_pb2 as transaction_pb2
import common.transaction_pb2_grpc as transaction_pb2_grpc
import common.operation_pb2 as operation_pb2
import common.operation_pb2_grpc as operation_pb2_grpc
import db
from statistic.models import Transactions, Operations

app = FastAPI()

session = db.get_db()
Base = declarative_base()


class Transaction(BaseModel):
    id: str
    email: str
    password: str
    identification_number: str


class TransactionServicer(transaction_pb2_grpc.TransactionServicer):
    def create_transaction(self, request):
        session = db.get_db()
        db_transaction = Transactions(id=request.id, operation_id=request.operation_id, description=request.description)
        session.add(db_transaction)
        db.close_db(session)
        return transaction_pb2.Transaction(id=db_transaction.id, operation_id=db_transaction.operation_id, description=db_transaction.description)


class OperationServicer(operation_pb2_grpc.OperationServicer):
    def create_operation(self, request):
        session = db.get_db()
        db_operation = Operations(id=request.id, status=request.status)
        session.add(db_operation)
        db.close_db()
        return operation_pb2.Operation(id=db_operation.id, status=db_operation.status)

    def update_operation_status(self, request, context):
        session = db.get_db()
        db_operation = session.query(Operations).filter(Operations.id == request.id).first()
        if db_operation:
            db_operation.status = request.status
            db.close_db()
            return operation_pb2.Operation(id=db_operation.id, status=db_operation.status)
        else:
            context.set_details("Operation not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return operation_pb2.Operation()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transaction_pb2_grpc.add_TransactionServicer_to_server(TransactionServicer(), server)
    operation_pb2_grpc.add_OperationServicer_to_server(OperationServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
