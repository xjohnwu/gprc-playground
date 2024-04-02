# xjohnwu-gprc-playground

1. Create a file named `orderbook.proto` to define the order book message and the gPRC service
2. Generate the gRPC code using the `protoc` compiler
    ```bash
    python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./proto/orderbook.proto
    ```
3. Implement the gRPC server in Python
4. Implement the gRPC client in Python