"""BaseModel for a Title Slide"""

from pydantic import BaseModel


class TitleSlide(BaseModel):
    """BaseModel for a PowerPoint Title Slide."""

    title: str
    subtitle: str
    layout: str = "Title Slide"
    title_font_size: int = 54
    subtitle_font_size: int = 32
    title_font_name: str = "Calibri"
    subtitle_font_name: str = "Calibri Light"
    title_color: str = "#000000"  # Black
    subtitle_color: str = "#333333"  # Dark gray
    background_color: str = "#FFFFFF"  # White
    title_alignment: str = "center"
    subtitle_alignment: str = "center"
    title_bold: bool = True
    subtitle_bold: bool = False
    title_margin_top: float = 0.3  # As a percentage of slide height
    subtitle_margin_top: float = 0.6
    margin_left: float = 0.05
    margin_right: float = 0.05
