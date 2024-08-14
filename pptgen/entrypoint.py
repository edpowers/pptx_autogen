"""Entrypoint."""

from pathlib import Path

import pandas as pd
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


def generate_ppt(
    company_name: str, subtitle_company: str, csv_data_path: Path, output_file: Path
) -> Path:
    """
    Generate a PowerPoint presentation based on the given CSV data.

    Args:
    csv_data_path (Path): Path to the CSV file.
    company_name (str): Name of the company.
    subtitle_company (str): Subtitle for the company.
    output_dir (Path): Directory to save the output PPTX file.

    Returns:
    Path: Path to the generated PPTX file.
    """
    # Read CSV data
    df = pd.read_csv(csv_data_path)

    # Get the metadata
    columns_meta = get_dataframe_metadata(df)

    # Create a presentation
    prs = Presentation()

    color_scheme = ThemeColorScheme(theme=ColorTheme.PROFESSIONAL_TEST)

    # Create a TitleSlide model
    title_slide_model = TitleSlide(
        title=f"UCC Data - {company_name.upper()}",
        subtitle=subtitle_company,
    )

    # Add title slide
    add_title_slide(prs, title_slide_model, color_scheme)

    # Add overview slide
    create_overview_slide(df, prs, color_scheme, company_name)

    # Generate slides based on the number of columns
    if len(columns_meta.columns) > 10:
        print("Creating consolidated view")
        create_consolidated_view(columns_meta, prs, color_scheme)
    else:
        create_detailed_view(columns_meta, prs, color_scheme)

    # Create PPTXModel and write to file
    pptx_model = PPTXModel(file_name=str(output_file), pptx_raw=prs)
    pptx_model.write_pptx()

    return output_file
