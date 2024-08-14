"""Color Functions."""

from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Pt


def hex_to_rgb(hex_color: str) -> tuple[int, ...]:
    """Convert hex color to RGB tuple."""
    return tuple(int(hex_color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))


def apply_text_gradient(paragraph, gradient, font_size, font_name):
    """Apply gradient to text."""
    paragraph.font.size = Pt(font_size)
    paragraph.font.name = font_name

    # Apply gradient to text
    start_color, end_color = gradient
    fill = paragraph.font.fill
    fill.gradient()
    fill.gradient_stops[0].color.rgb = RGBColor(*hex_to_rgb(start_color))
    fill.gradient_stops[1].color.rgb = RGBColor(*hex_to_rgb(end_color))


def apply_background_gradient(slide, gradient):
    """Apply gradient to slide background."""
    background = slide.background
    fill = background.fill
    fill.gradient()
    start_color, end_color = gradient
    fill.gradient_stops[0].color.rgb = RGBColor(*hex_to_rgb(start_color))
    fill.gradient_stops[1].color.rgb = RGBColor(*hex_to_rgb(end_color))
    fill.gradient_angle = 45  # You can adjust this angle as needed


def apply_text_formatting(
    paragraph,
    color,
    font_size,
    font_name,
    bold=False,
    italic=False,
    alignment=PP_ALIGN.LEFT,
):
    """Apply high-quality text formatting to a paragraph."""
    run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
    font = run.font
    font.name = font_name
    font.size = Pt(font_size)

    # Remove '#' from color string if present
    if color:
        color = color.lstrip("#")
        font.color.rgb = RGBColor.from_string(color)
    else:
        font.color.rgb = RGBColor(0, 0, 0)

    font.bold = bold
    font.italic = italic
    paragraph.alignment = alignment
