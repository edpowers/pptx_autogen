"""Example usage."""

# %%

from pptgen.model.color_themes import ThemeColorScheme, ColorTheme
from pptgen.model.content_slide import ContentSlide
from pptgen.model.image_slide import ImageSlide
from pptgen.model.title_slide import TitleSlide

from pptgen.model.base_paths import BasePaths
from pptgen.model.pptx_model import PPTXModel

from pptgen.create_presentation import create_presentation

# %%


# %%

# Create a presentation
base_paths = BasePaths()
# Usage example:
color_scheme = ThemeColorScheme(theme=ColorTheme.CHRISTMAS)

slides = [
    TitleSlide(title="Christmas Presentation", subtitle="Happy Holidays!"),
    ContentSlide(
        title="Winter Facts",
        content="1. Snow is white\n2. It's cold\n3. People build snowmen",
    ),
    ImageSlide(
        title="Christmas Tree",
        image_path=str(base_paths.image_path.joinpath("christmas_tree.jpg").resolve()),
    ),
]

pptx_file = create_presentation(slides, color_scheme)


pptx_file_christmas = PPTXModel(
    file_name="Christmas_Presentation.pptx", pptx=pptx_file.get_value()
)

pptx_file_christmas.write_pptx()

# %%
