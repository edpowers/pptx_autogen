"""Example usage."""

# %%

import pprint
import sys

from pptgen.create_presentation import create_presentation
from pptgen.model.base_paths import BasePaths
from pptgen.model.powerpoint.color_themes import ColorTheme, ThemeColorScheme
from pptgen.model.powerpoint.common import BulletPoint, BulletPoints
from pptgen.model.powerpoint.content_slide import ContentSlide
from pptgen.model.powerpoint.image_slide import ImageSlide
from pptgen.model.powerpoint.title_slide import TitleSlide
from pptgen.model.pptx_model import PPTXModel

pprint.pprint(sys.path)

# %%


# %%

# Create a presentation
base_paths = BasePaths()
# Usage example:
color_scheme = ThemeColorScheme(theme=ColorTheme.CHRISTMAS)

# Define BulletPoints for the ContentSlide
winter_facts = BulletPoints(
    bullet_points=[
        BulletPoint(text="Snow is white"),
        BulletPoint(text="It's cold"),
        BulletPoint(text="People build snowmen"),
    ]
)

slides = [
    TitleSlide(title="Christmas Presentation", subtitle="Happy Holidays!"),
    ContentSlide(
        title="Winter Facts",
        content=winter_facts,
    ),
    ImageSlide(
        title="Christmas Tree",
        image_path=base_paths.find_image("christmas_tree"),
    ),
]

pptx_file = create_presentation(slides, color_scheme)


pptx_file_christmas = PPTXModel(
    file_name="Christmas_Presentation.pptx", pptx_raw=pptx_file
)

pptx_file_christmas.write_pptx()

# %%
