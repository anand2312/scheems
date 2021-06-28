import datetime
from typing import Mapping, Optional, Sequence, Type

from pydantic import BaseModel
from sqlalchemy import Table
from sqlalchemy.sql import sqltypes
from sqlalchemy.types import TypeEngine

from .exceptions import UnsupportedTypeError


def _get_type(_type: TypeEngine) -> Type:
    """Gets corresponding type for SQLAlchemy column types that can be used in pydantic fields."""
    types_map: Mapping[Type[TypeEngine], Type] = {
        sqltypes.Text: str,
        sqltypes.String: str,
        sqltypes.Integer: int,
        sqltypes.BigInteger: int,
        sqltypes.SmallInteger: int,
        sqltypes.Boolean: bool,
        sqltypes.Date: datetime.date,
        sqltypes.DateTime: datetime.datetime,
        sqltypes.Interval: datetime.timedelta,
        sqltypes.Time: datetime.time,
        sqltypes.Float: float,
    }

    try:
        return types_map[_type]  # type: ignore ; # TODO: find out why
    except KeyError as e:
        raise UnsupportedTypeError(
            f"Type {_type} is not currently supported by Scheems. Please make an issue at https://github.com/anand2312/scheems/issues to add it."
        ) from e


def _check_columns_with_table(table: Table, columns: Sequence[str]) -> Optional[bool]:
    """Checks whether the `columns` passed in all belong to the `table`."""
    for column in columns:
        if column not in table.c.keys():
            raise TypeError(f"Specified column {column} did not exist on table {table}")
    return True


def get_filter_model(table: Table, allowed_filters: Sequence[str]) -> Type[BaseModel]:
    """
    Returns a pydantic model that will be used to validate requests/responses with query filters
    specified, for the given table.

    Type are inferred based on the data types defined
    in the table.

    Arguments:
        table: The table for which the model should be made
        allowed_filters: List of columns by which data can be filtered.

    Returns:
        A pydantic model.
    """
    _check_columns_with_table(table, allowed_filters)

    annotations = {}

    for column in allowed_filters:
        column_obj = table.c[column]
        type_hint = _get_type(column_obj.type)
        annotations[column] = Optional[
            type_hint
        ]  # optional as all columns may not be passed

    return type(table.name, (BaseModel,), {"__annotations__": annotations})
