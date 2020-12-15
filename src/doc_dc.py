from dataclasses import fields, asdict
from typing import TypeVar

import azure.functions as func

DataClass = TypeVar("DataClass")


def doc2dc(doc: func.Document, dc: DataClass) -> DataClass:
    """Convert a Azure Document to the `dataclass` you want.

    Args:
        doc (func.Document): An Azure Document.
        dc (DataClass): A dataclass you want to convert the document.

    Returns:
        DataClass: A dataclass given as the 2nd arg.
    
    Examples:
        >>> @dataclass
        >>> class User:
        >>>     name: str
        >>>     age: int
        >>> 
        >>> user = doc2dc(doc, User)
        >>> print(user.name, user.id)
        ```
    """
    args = list(map(lambda x: x.name, fields(dc)))
    values = tuple(map(lambda x: doc[x], args))
    return dc(*values)


def dc2doc(dc: DataClass) -> func.Document:
    """Convert a dataclass to an Azure Document.

    Args:
        dc (DataClass): A dataclass.

    Returns:
        func.Document: An Azure Document.
    
    Examples:
        >>> @dataclass
        >>> class User:
        >>>     name: str
        >>>     age: int
        >>> 
        >>> user = User("syakoo", 22) # User(name='syakoo', age=22)
        >>> doc = dc2doc(user) # <azure.Document at 0x7f189f516160>
    """
    return func.Document.from_dict(asdict(dc))