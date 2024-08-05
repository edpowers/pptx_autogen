"""Make a powerpoint for a DataFrame."""
# %%

import os
from pathlib import Path

import pandas as pd
from dotenv import find_dotenv, load_dotenv
from pptx import Presentation

from pptgen.create_presentation import add_title_slide
from pptgen.generate_dataframe_meta import (
    create_consolidated_view,
    create_detailed_view,
    create_overview_slide,
    get_dataframe_metadata,
)
from pptgen.model.powerpoint import ColorTheme, ThemeColorScheme, TitleSlide
from pptgen.model.pptx_model import PPTXModel

load_dotenv(find_dotenv(raise_error_if_not_found=True))

# %%

CSV_DATA_PATH = Path(os.getenv("CSV_DATA_PATH"))
COMPANY_NAME = os.getenv("COMPANY_NAME")
SUBTITLE_COMPANY = os.getenv("SUBTITLE_COMPANY")

df = pd.read_csv(CSV_DATA_PATH.joinpath(f"{COMPANY_NAME}.csv"))

# %%

# Get the metadata
columns_meta = get_dataframe_metadata(df)

# Create a presentation
prs = Presentation()
color_scheme = ThemeColorScheme(theme=ColorTheme.PROFESSIONAL_TEST)

# Create a TitleSlide model
title_slide_model = TitleSlide(
    title=f"UCC Data - {COMPANY_NAME.upper()}",
    subtitle=SUBTITLE_COMPANY,
)

# Add title slide
add_title_slide(prs, title_slide_model, color_scheme)

# Add overview slide
create_overview_slide(df, prs, color_scheme, COMPANY_NAME)

# Generate slides based on the number of columns
if len(columns_meta.columns) > 10:
    print("Creating consolidated view")
    slides = create_consolidated_view(columns_meta, prs, color_scheme)
else:
    slides = create_detailed_view(columns_meta, prs, color_scheme)

# %%


pptx_snapon = PPTXModel(file_name=f"{COMPANY_NAME}.pptx", pptx_raw=prs)

pptx_snapon.write_pptx()


# %%
