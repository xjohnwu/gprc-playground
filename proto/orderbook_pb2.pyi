from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderBook(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("id", "price", "quantity", "side")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    id: str
    price: float
    quantity: float
    side: str
    def __init__(self, id: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[float] = ..., side: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
