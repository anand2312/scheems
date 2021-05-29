import datetime
from typing import Mapping, Type

from pydantic import BaseModel
from sqlalchemy import Table
from sqlalchemy.sql import sqltypes
from sqlalchemy.types import TypeEngine


def _get_type(_type: Type[TypeEngine]) -> Type:
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

    return types_map[_type]


def get_request_model(table: Table) -> Type[BaseModel]:
    """
    Returns a pydantic model that will be used to validate requests for the given table.

    Type are inferred based on the data types defined
    in the table.

    Arguments:
        table: The table for which the model should be made
    Returns:
        A pydantic model.
    """
    pass
