from typing import Any

class ListMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getitem__(self, index: Any) -> Any: ...
    def __delitem__(self, index: Any) -> None: ...
    def __setitem__(self, index: Any, val: Any) -> None: ...
    def __add__(self, other: Any) -> Any: ...
    def __radd__(self, other: Any) -> Any: ...
    def __iadd__(self, other: Any) -> Any: ...
    def __mul__(self, n: Any) -> Any: ...
    def __rmul__(self, n: Any) -> Any: ...
    def __imul__(self, n: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def count(self, val: Any) -> Any: ...
    def index(self, val: Any) -> Any: ...
    def append(self, val: Any) -> None: ...
    def extend(self, vals: Any) -> None: ...
    def insert(self, index: Any, val: Any) -> None: ...
    def pop(self, index: int = ...) -> Any: ...
    def remove(self, val: Any) -> None: ...
    def reverse(self) -> None: ...
    def sort(self, key: Any | None = ..., reverse: bool = ...) -> None: ...
