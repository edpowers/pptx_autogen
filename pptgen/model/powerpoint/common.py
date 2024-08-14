"""BulletPoints."""

from pydantic import BaseModel

from typing import List


class BulletPoint(BaseModel):
    """BaseModel for a Bullet Point."""

    text: str
    font_size: int = 32
    font_name: str = "Arial"


class BulletPoints(BaseModel):
    """BaseModel for a Bullet Points Slide."""

    bullet_points: List[BulletPoint]
