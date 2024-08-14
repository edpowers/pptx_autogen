"""Pydantic Models for DataFrame Column Metadata."""

from typing import List

from pydantic import BaseModel


class ColumnMeta(BaseModel):
    column: str
    type: str
    non_null_count: int
    null_count: int
    unique_values: int


class ColumnsMeta(BaseModel):
    columns: List[ColumnMeta]
