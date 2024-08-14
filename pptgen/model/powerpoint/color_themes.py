from enum import Enum
from typing import Dict, Optional, Tuple

from pydantic import BaseModel


class ColorTheme(str, Enum):
    PROFESSIONAL = "professional"
    PROFESSIONAL_TEST = "professional_test"
    VIBRANT = "vibrant"
    PASTEL = "pastel"
    DARK = "dark"
    CHRISTMAS = "christmas"


class ColorMixin(BaseModel):
    """Color mixin for PowerPoint slides to set master colors."""

    title_color: Optional[str] = None
    subtitle_color: Optional[str] = None
    content_color: Optional[str] = None
    accent_gradient_1: Optional[Tuple[str, str]] = None
    accent_gradient_2: Optional[Tuple[str, str]] = None
    accent_gradient_3: Optional[Tuple[str, str]] = None
    accent_gradient_4: Optional[Tuple[str, str]] = None
    accent_gradient_5: Optional[Tuple[str, str]] = None
    accent_gradient_6: Optional[Tuple[str, str]] = None
    primary_gradient: Optional[Tuple[str, str]] = None  # TODO - remove
    secondary_gradient: Optional[Tuple[str, str]] = None  # TODO - remove
    background_gradient: Optional[Tuple[str, str]] = None

    def apply_colors(self, slide_model: BaseModel) -> None:
        """Apply color settings to a slide model."""
        for field, value in self.dict(exclude_unset=True).items():
            if value is not None and hasattr(slide_model, field):
                setattr(slide_model, field, value)

        # Apply solid colors to title, subtitle, and content
        if self.title_color and hasattr(slide_model, "title_color"):
            slide_model.title_color = self.title_color
        if self.subtitle_color and hasattr(slide_model, "subtitle_color"):
            slide_model.subtitle_color = self.subtitle_color
        if self.content_color and hasattr(slide_model, "content_color"):
            slide_model.content_color = self.content_color


class ThemeColorScheme(ColorMixin):
    """Theme-based color scheme for PowerPoint presentation."""

    theme: ColorTheme

    @classmethod
    def get_theme_colors(cls) -> Dict[ColorTheme, Dict[str, Tuple[str, str]]]:
        return {
            ColorTheme.PROFESSIONAL: {
                "primary_gradient": ("#000000", "#333333"),
                "secondary_gradient": ("#FFFFFF", "#F0F0F0"),
                "accent_gradient_1": ("#0066CC", "#003366"),
                "accent_gradient_2": ("#ED7D31", "#C45A1A"),
                "accent_gradient_3": ("#A5A5A5", "#808080"),
                "accent_gradient_4": ("#FFC000", "#D9A300"),
                "accent_gradient_5": ("#5B9BD5", "#3F7DAD"),
                "accent_gradient_6": ("#70AD47", "#4F7A32"),
                "background_gradient": ("#F2F2F2", "#E6E6E6"),
            },
            ColorTheme.PROFESSIONAL_TEST: {
                "title_color": "#333333",  # Dark gray for title
                "subtitle_color": "#666666",  # Medium gray for subtitle
                "content_color": "#333333",  # Dark gray for content
                "primary_gradient": (
                    "#000000",
                    "#333333",
                ),  # TODO: remove from pydantic model.
                "accent_gradient_1": ("#0066CC", "#0080FF"),  # Blue
                "accent_gradient_2": ("#008080", "#00A3A3"),  # Teal
                "accent_gradient_3": ("#6B8E23", "#8AB33B"),  # Olive Green
                "accent_gradient_4": ("#4B0082", "#6600B3"),  # Indigo
                "accent_gradient_5": ("#8B4513", "#B35A1A"),  # Sienna (Brown)
                "accent_gradient_6": ("#708090", "#8C9CAA"),  # Slate Gray
                "background_gradient": (
                    "#F8F8F8",
                    "#F0F0F0",
                ),  # Very light gray background
            },
            ColorTheme.VIBRANT: {
                "primary_gradient": ("#FFFFFF", "#F0F0F0"),
                "secondary_gradient": ("#000000", "#333333"),
                "accent_gradient_1": ("#FF4136", "#CC3328"),
                "accent_gradient_2": ("#FF851B", "#CC6A16"),
                "accent_gradient_3": ("#FFDC00", "#CCB000"),
                "accent_gradient_4": ("#2ECC40", "#25A333"),
                "accent_gradient_5": ("#0074D9", "#005CAD"),
                "accent_gradient_6": ("#B10DC9", "#8E0AA1"),
                "background_gradient": ("#001F3F", "#001326"),
            },
            ColorTheme.PASTEL: {
                "primary_gradient": ("#5D5C61", "#4A494D"),
                "secondary_gradient": ("#FFFFFF", "#F0F0F0"),
                "accent_gradient_1": ("#B1A296", "#8E8279"),
                "accent_gradient_2": ("#F7CAC9", "#EFA7A5"),
                "accent_gradient_3": ("#92A8D1", "#7589B8"),
                "accent_gradient_4": ("#AED9E0", "#8BBFC8"),
                "accent_gradient_5": ("#FFA69E", "#FF7D73"),
                "accent_gradient_6": ("#FAF3DD", "#F5EAB8"),
                "background_gradient": ("#EAE7DC", "#D8D3C4"),
            },
            ColorTheme.DARK: {
                "primary_gradient": ("#FFFFFF", "#F0F0F0"),
                "secondary_gradient": ("#CCCCCC", "#A6A6A6"),
                "accent_gradient_1": ("#BB86FC", "#9965D3"),
                "accent_gradient_2": ("#03DAC6", "#02A899"),
                "accent_gradient_3": ("#3700B3", "#2B008C"),
                "accent_gradient_4": ("#CF6679", "#B84D5D"),
                "accent_gradient_5": ("#018786", "#015F5F"),
                "accent_gradient_6": ("#B00020", "#8C0019"),
                "background_gradient": ("#121212", "#0A0A0A"),
            },
            ColorTheme.CHRISTMAS: {
                "primary_gradient": ("#FFFFFF", "#F0F0F0"),
                "secondary_gradient": ("#FFD700", "#CCAC00"),
                "accent_gradient_1": ("#CC0000", "#990000"),
                "accent_gradient_2": ("#006400", "#004D00"),
                "accent_gradient_3": ("#1A5F7A", "#134759"),
                "accent_gradient_4": ("#C41E3A", "#9A172D"),
                "accent_gradient_5": ("#00A86B", "#007A4D"),
                "accent_gradient_6": ("#8B4513", "#663311"),
                "background_gradient": ("#0C3823", "#09291A"),
            },
        }

    def __init__(self, **data):
        super().__init__(**data)
        theme_colors = self.get_theme_colors()[self.theme]
        for key, value in theme_colors.items():
            if getattr(self, key) is None:
                setattr(self, key, value)
