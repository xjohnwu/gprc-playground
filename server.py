from concurrent import futures
import grpc

from proto import orderbook_pb2_grpc, orderbook_pb2


class OrderBookService(orderbook_pb2_grpc.OrderBookServiceServicer):
    def GetOrderBook(self, request, context):
        order_book = orderbook_pb2.OrderBook(
            orders=[
                orderbook_pb2.Order(id="1", price=100.0, quantity=10.0, side="buy"),
                orderbook_pb2.Order(id="2", price=101.0, quantity=5.0, side="sell"),
            ]
        )
        return order_book


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orderbook_pb2_grpc.add_OrderBookServiceServicer_to_server(OrderBookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
