from dataclasses import dataclass
from typing import ClassVar

from rhyolite import from_dict


def test_from_dict_with_correct_data():
    @dataclass
    class X:
        s: ClassVar[str] = "Hello, World!"
        i: int
        f: float

    result = from_dict(X, {"s": "test", "i": 1, "f": 1.0})

    assert result == X(i=1, f=1.0)
    assert "Hello, World!" == X.s
