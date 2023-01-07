from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Price(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: float
    def __init__(self, price: _Optional[float] = ...) -> None: ...

class Prices(_message.Message):
    __slots__ = ["prices"]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    prices: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, prices: _Optional[_Iterable[float]] = ...) -> None: ...

class Vintage(_message.Message):
    __slots__ = ["serialized_vintage"]
    SERIALIZED_VINTAGE_FIELD_NUMBER: _ClassVar[int]
    serialized_vintage: str
    def __init__(self, serialized_vintage: _Optional[str] = ...) -> None: ...

class VintageID(_message.Message):
    __slots__ = ["vintage_id"]
    VINTAGE_ID_FIELD_NUMBER: _ClassVar[int]
    vintage_id: str
    def __init__(self, vintage_id: _Optional[str] = ...) -> None: ...

class VintageIDs(_message.Message):
    __slots__ = ["vintage_ids"]
    VINTAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    vintage_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vintage_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class VintageTitle(_message.Message):
    __slots__ = ["vintage_title"]
    VINTAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
    vintage_title: str
    def __init__(self, vintage_title: _Optional[str] = ...) -> None: ...

class VintageTitles(_message.Message):
    __slots__ = ["vintage_titles"]
    VINTAGE_TITLES_FIELD_NUMBER: _ClassVar[int]
    vintage_titles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vintage_titles: _Optional[_Iterable[str]] = ...) -> None: ...

class Vintages(_message.Message):
    __slots__ = ["serialized_vintages"]
    SERIALIZED_VINTAGES_FIELD_NUMBER: _ClassVar[int]
    serialized_vintages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, serialized_vintages: _Optional[_Iterable[str]] = ...) -> None: ...

class WineID(_message.Message):
    __slots__ = ["wine_id"]
    WINE_ID_FIELD_NUMBER: _ClassVar[int]
    wine_id: str
    def __init__(self, wine_id: _Optional[str] = ...) -> None: ...

class WineIDs(_message.Message):
    __slots__ = ["wine_ids"]
    WINE_IDS_FIELD_NUMBER: _ClassVar[int]
    wine_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, wine_ids: _Optional[_Iterable[str]] = ...) -> None: ...
