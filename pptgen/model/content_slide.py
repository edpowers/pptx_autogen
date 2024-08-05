"""Base Model for a Graphic Content Slide."""

from pydantic import BaseModel


class ContentSlide(BaseModel):
    """BaseModel for a PowerPoint Content Slide."""

    title: str
    content: str
    layout: str = "Content with Caption"
    title_font_size: int = 40
    content_font_size: int = 24
    title_font_name: str = "Calibri"
    content_font_name: str = "Calibri"
    title_color: str = "#000000"  # Black
    content_color: str = "#000000"  # Black
    background_color: str = "#FFFFFF"  # White
    title_alignment: str = "left"
    content_alignment: str = "left"
    margin_top: float = 0.1  # As a percentage of slide height
    margin_bottom: float = 0.1
    margin_left: float = 0.05
    margin_right: float = 0.05
