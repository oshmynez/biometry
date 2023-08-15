import time
from concurrent import futures

import grpc
from fastapi import FastAPI

import common.operation_pb2 as operation_pb2
import common.operation_pb2_grpc as operation_pb2_grpc
import common.transaction_pb2 as transaction_pb2
import common.transaction_pb2_grpc as transaction_pb2_grpc
from session import close_db, get_db
from statistic.db import Operations, Transactions

app = FastAPI()


class TransactionServicer(transaction_pb2_grpc.TransactionServicer):
    def create_transaction(self, request):
        session = get_db()
        db_transaction = Transactions(id=request.id, operation_id=request.operation_id, description=request.description)
        session.add(db_transaction)
        close_db(session)
        return transaction_pb2.Transaction(id=db_transaction.id, operation_id=db_transaction.operation_id, description=db_transaction.description)


class OperationServicer(operation_pb2_grpc.OperationServicer):
    def create_operation(self, request):
        session = get_db()
        db_operation = Operations(id=request.id, status=request.status)
        session.add(db_operation)
        close_db()
        return operation_pb2.Operation(id=db_operation.id, status=db_operation.status)

    def update_operation_status(self, request, context):
        session = get_db()
        db_operation = session.query(Operations).filter(Operations.id == request.id).first()
        if db_operation:
            db_operation.status = request.status
            close_db()
            return operation_pb2.Operation(id=db_operation.id, status=db_operation.status)
        else:
            context.set_details("Operation not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return operation_pb2.Operation()


def serve():
    try:
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
    except Exception as ex:
        print(ex)



if __name__ == "__main__":
    serve()
