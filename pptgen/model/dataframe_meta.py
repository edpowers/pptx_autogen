"""Pydantic Models for DataFrame Column Metadata."""

from pydantic import BaseModel
from typing import List


class ColumnMeta(BaseModel):
    column: str
    type: str
    non_null_count: int
    null_count: int
    unique_values: int


class ColumnsMeta(BaseModel):
    columns: List[ColumnMeta]
