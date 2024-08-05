from pydantic import BaseModel
from typing import Optional, Dict
from enum import Enum


# Usage example:
# christmas_theme = ThemeColorScheme(theme=ColorTheme.CHRISTMAS)
#
# Apply to a slide
# title_slide = PowerPointTitleSlide(
#    title="Merry Christmas!",
#    subtitle="Season's Greetings"
# )
# christmas_theme.apply_colors(title_slide)


class ColorTheme(str, Enum):
    PROFESSIONAL = "professional"
    VIBRANT = "vibrant"
    PASTEL = "pastel"
    DARK = "dark"
    CHRISTMAS = "christmas"


class ColorMixin(BaseModel):
    """Color mixin for PowerPoint slides to set master colors."""

    primary_color: Optional[str] = None
    secondary_color: Optional[str] = None
    accent_color_1: Optional[str] = None
    accent_color_2: Optional[str] = None
    accent_color_3: Optional[str] = None
    accent_color_4: Optional[str] = None
    accent_color_5: Optional[str] = None
    accent_color_6: Optional[str] = None
    background_color: Optional[str] = None

    def apply_colors(self, slide_model: BaseModel):
        """Apply color settings to a slide model."""
        for field, value in self.dict(exclude_unset=True).items():
            if value is not None and hasattr(slide_model, field):
                setattr(slide_model, field, value)

        # Apply primary color to title and content
        if self.primary_color:
            if hasattr(slide_model, "title_color"):
                slide_model.title_color = self.primary_color
            if hasattr(slide_model, "content_color"):
                slide_model.content_color = self.primary_color
        if self.secondary_color and hasattr(slide_model, "subtitle_color"):
            slide_model.subtitle_color = self.secondary_color


class ThemeColorScheme(ColorMixin):
    """Theme-based color scheme for PowerPoint presentation."""

    theme: ColorTheme

    @classmethod
    def get_theme_colors(cls) -> Dict[ColorTheme, Dict[str, str]]:
        return {
            ColorTheme.PROFESSIONAL: {
                "primary_color": "#000000",
                "secondary_color": "#FFFFFF",
                "accent_color_1": "#0066CC",
                "accent_color_2": "#ED7D31",
                "accent_color_3": "#A5A5A5",
                "accent_color_4": "#FFC000",
                "accent_color_5": "#5B9BD5",
                "accent_color_6": "#70AD47",
                "background_color": "#F2F2F2",
            },
            ColorTheme.VIBRANT: {
                "primary_color": "#FFFFFF",
                "secondary_color": "#000000",
                "accent_color_1": "#FF4136",
                "accent_color_2": "#FF851B",
                "accent_color_3": "#FFDC00",
                "accent_color_4": "#2ECC40",
                "accent_color_5": "#0074D9",
                "accent_color_6": "#B10DC9",
                "background_color": "#001F3F",
            },
            ColorTheme.PASTEL: {
                "primary_color": "#5D5C61",
                "secondary_color": "#FFFFFF",
                "accent_color_1": "#B1A296",
                "accent_color_2": "#F7CAC9",
                "accent_color_3": "#92A8D1",
                "accent_color_4": "#AED9E0",
                "accent_color_5": "#FFA69E",
                "accent_color_6": "#FAF3DD",
                "background_color": "#EAE7DC",
            },
            ColorTheme.DARK: {
                "primary_color": "#FFFFFF",
                "secondary_color": "#CCCCCC",
                "accent_color_1": "#BB86FC",
                "accent_color_2": "#03DAC6",
                "accent_color_3": "#3700B3",
                "accent_color_4": "#CF6679",
                "accent_color_5": "#018786",
                "accent_color_6": "#B00020",
                "background_color": "#121212",
            },
            ColorTheme.CHRISTMAS: {
                "primary_color": "#FFFFFF",
                "secondary_color": "#FFD700",
                "accent_color_1": "#CC0000",
                "accent_color_2": "#006400",
                "accent_color_3": "#1A5F7A",
                "accent_color_4": "#C41E3A",
                "accent_color_5": "#00A86B",
                "accent_color_6": "#8B4513",
                "background_color": "#0C3823",
            },
        }

    def __init__(self, **data):
        super().__init__(**data)
        theme_colors = self.get_theme_colors()[self.theme]
        for key, value in theme_colors.items():
            if getattr(self, key) is None:
                setattr(self, key, value)
