from typing import Any, Literal, Mapping, Optional, Sequence, Type, Union

from pydantic import BaseModel
from sqlalchemy import Table
from sqlalchemy.orm.decl_api import DeclarativeMeta
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response

from scheems.exceptions import MissingRequiredParameter


Methods = Union[
    Literal["GET"], Literal["POST"], Literal["DELETE"]
]  # only these methods are allowed


def scheems_route(
    table: Union[DeclarativeMeta, Table],
    *,
    identified_by: Optional[str] = "pkey",
    methods: Optional[Sequence[Methods]] = ("GET",),
    allow_bulk: bool = False,
    allowed_filters: Sequence[str] = None,
) -> Route:
    """
    Defines a route on the scheems API based on the provided `table`.

    # TODO: complete doc
    """
    if isinstance(table, DeclarativeMeta):
        table = table.__table__  # type: ignore ; in case a declared model was sent, use it's underlying table object

    if not identified_by:
        identifier = table.primary_key  # type: ignore ; if not passed, use primary key column
    else:
        identifier = table.c[identified_by]  # type: ignore


async def _get_identifier_callback(
    request: Request, identified_by: str, model: Type[BaseModel]
) -> Response:
    """
    Generic callback function for the `/model/{identifier} route.
    To be used along with `functools.partial` to provide the model and identifier.
    """
    try:
        identifier_value = request.path_params[identified_by]
    except KeyError:
        raise MissingRequiredParameter(
            f"Required parameter {identified_by} was not provided."
        )
