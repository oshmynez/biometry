cd common
python -m grpc_tools.protoc -I. --python_out=./statistic --grpc_python_out=./statistic ./common/transaction.proto ./common/operation.proto
