from typing import Literal, Sequence, Union

from sqlalchemy import Table
from starlette.routing import Route


Methods = Union[
    Literal["GET"], Literal["POST"], Literal["DELETE"]
]  # only these methods are allowed


def scheems_route(
    table: Table, *, identified_by: str = None, methods: Sequence[Methods] = ("GET",)
) -> Route:
    """
    Defines a route on the scheems API based on the provided `table`.

    # TODO: complete doc
    """
    if not identified_by:
        identifier = table.primary_key  # if not passed, use primary key column
    else:
        identifier = table.c[identified_by]
    identifier
    ...
