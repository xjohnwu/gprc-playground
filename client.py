import grpc

from proto import orderbook_pb2_grpc, orderbook_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = orderbook_pb2_grpc.OrderBookServiceStub(channel)
        response = stub.GetOrderBook(orderbook_pb2.Empty())
        print("OrderBook received: ")
        for order in response.orders:
            print(f"Order ID: {order.id}, Price: {order.price}, Quantity: {order.quantity}, Side: {order.side}")


if __name__ == '__main__':
    run()
