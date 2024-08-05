"""Pydantic model for an image slide."""

from pathlib import Path

from pydantic import BaseModel


class ImageSlide(BaseModel):
    """Pydantic model for a PowerPoint Image Slide."""

    title: str
    image_path: str
    layout: str = "Picture with Caption"
    title_font_size: int = 40
    title_font_name: str = "Calibri"
    title_color: str = "#000000"  # Black
    background_color: str = "#FFFFFF"  # White
    title_alignment: str = "center"
    title_bold: bool = True
    image_horizontal_alignment: str = "center"
    image_vertical_alignment: str = "center"
    title_margin_top: float = 0.05  # As a percentage of slide height
    image_margin_top: float = 0.15
    image_width: float = 0.8  # As a percentage of slide width
    image_height: float = 0.7  # As a percentage of slide height
    margin_left: float = 0.05
    margin_right: float = 0.05
