from typing import Any, Union, Callable, Optional


def is_sorted(items: list[Any]) -> bool:
    # for i in range(len(items) - 1):
    #     if items[i] > items[i + 1]:
    #         return False
    # return True
    for a, b in zip(items, items[1:]):
        if a > b:
            return False
    return True


def getitem(obj: Any, key: Optional[Any] = None) -> Union[Any, Callable[[Any], Any]]:
    if key is not None:
        return obj[key]

    key = obj
    return lambda o: o[key]
