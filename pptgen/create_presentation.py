"""Construct Powerpoint."""

from typing import Any, List

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import io

from pptgen.model.content_slide import ContentSlide
from pptgen.model.image_slide import ImageSlide
from pptgen.model.title_slide import TitleSlide


def hex_to_rgb(hex_color: str) -> tuple[int, ...]:
    """Convert hex color to RGB tuple."""
    return tuple(int(hex_color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))


def add_title_slide(prs, slide_model, color_scheme):
    """Add a title slide to the presentation."""
    layout = prs.slide_layouts[0]  # Title Slide layout
    slide = prs.slides.add_slide(layout)

    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = slide_model.title
    subtitle.text = slide_model.subtitle

    # Apply text properties
    title.text_frame.paragraphs[0].font.size = Pt(slide_model.title_font_size)
    title.text_frame.paragraphs[0].font.name = slide_model.title_font_name
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(
        *hex_to_rgb(color_scheme.primary_color)
    )
    title.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

    subtitle.text_frame.paragraphs[0].font.size = Pt(slide_model.subtitle_font_size)
    subtitle.text_frame.paragraphs[0].font.name = slide_model.subtitle_font_name
    subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(
        *hex_to_rgb(color_scheme.secondary_color)
    )
    subtitle.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

    # Set background color
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(*hex_to_rgb(color_scheme.background_color))

    return slide


def add_content_slide(prs, slide_model, color_scheme):
    """Add a content slide to the presentation."""
    layout = prs.slide_layouts[1]  # Content with Caption layout
    slide = prs.slides.add_slide(layout)

    title = slide.shapes.title
    content = slide.placeholders[1]

    title.text = slide_model.title
    content.text = slide_model.content

    # Apply text properties
    title.text_frame.paragraphs[0].font.size = Pt(slide_model.title_font_size)
    title.text_frame.paragraphs[0].font.name = slide_model.title_font_name
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(
        *hex_to_rgb(color_scheme.primary_color)
    )
    title.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT

    for paragraph in content.text_frame.paragraphs:
        paragraph.font.size = Pt(slide_model.content_font_size)
        paragraph.font.name = slide_model.content_font_name
        paragraph.font.color.rgb = RGBColor(*hex_to_rgb(color_scheme.primary_color))
        paragraph.alignment = PP_ALIGN.LEFT

    # Set background color
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(*hex_to_rgb(color_scheme.background_color))

    return slide


def add_image_slide(prs, slide_model, color_scheme):
    """Add an image slide to the presentation."""
    layout = prs.slide_layouts[5]  # Picture with Caption layout
    slide = prs.slides.add_slide(layout)

    title = slide.shapes.title
    title.text = slide_model.title

    # Apply text properties
    title.text_frame.paragraphs[0].font.size = Pt(slide_model.title_font_size)
    title.text_frame.paragraphs[0].font.name = slide_model.title_font_name
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(
        *hex_to_rgb(color_scheme.primary_color)
    )
    title.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    title.text_frame.paragraphs[0].font.bold = True

    # Add image
    left = Inches(slide_model.margin_left)
    top = Inches(slide_model.image_margin_top)
    width = Inches(slide_model.image_width)
    height = Inches(slide_model.image_height)
    slide.shapes.add_picture(slide_model.image_path, left, top, width, height)

    # Set background color
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(*hex_to_rgb(color_scheme.background_color))

    return slide


def create_presentation(slide_models: List[Any], color_scheme) -> io.BytesIO:
    """Create a complete presentation based on slide models and color scheme."""
    prs = Presentation()

    for slide_model in slide_models:
        if isinstance(slide_model, TitleSlide):
            add_title_slide(prs, slide_model, color_scheme)
        elif isinstance(slide_model, ContentSlide):
            add_content_slide(prs, slide_model, color_scheme)
        elif isinstance(slide_model, ImageSlide):
            add_image_slide(prs, slide_model, color_scheme)

    # Save to a BytesIO object
    pptx_file = io.BytesIO()
    prs.save(pptx_file)
    pptx_file.seek(0)

    return pptx_file
