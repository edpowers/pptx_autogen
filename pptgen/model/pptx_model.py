"""Powerpoint model."""

import io
from pathlib import Path
from typing import Union

from pptx.presentation import Presentation
from pydantic import computed_field

from pptgen.model.base_paths import BasePaths


class PPTXModel(BasePaths):
    """Powerpoint model."""

    file_name: str
    pptx_raw: Union[bytes, io.BytesIO, Presentation]

    @computed_field
    @property
    def pptx_file(self) -> Path:
        """Get pptx file."""
        return self.output_path.joinpath(self.file_name).with_suffix(".pptx")

    @computed_field
    @property
    def pptx(self) -> bytes:
        """Get pptx."""
        return self.save_pptx_to_bytesio(self.pptx_raw).getvalue()

    def write_pptx(self) -> None:
        """Write pptx."""
        # Save the file
        with open(str(self.pptx_file), "wb") as f:
            f.write(self.pptx)

    def save_pptx_to_bytesio(self, prs: Union[io.BytesIO, Presentation]) -> io.BytesIO:
        if isinstance(prs, io.BytesIO):
            return prs
        # Save the presentation to a BytesIO object
        pptx_buffer = io.BytesIO()
        prs.save(pptx_buffer)
        pptx_buffer.seek(0)  # Move to the beginning of the BytesIO object

        return pptx_buffer

    def validate_output_exists(self) -> None:
        """Validate output exists."""
        if not self.pptx_file.exists():
            raise FileNotFoundError(f"Output file not found: {self.pptx_file}")

        print(f"Output file created: {self.pptx_file}")

    class Config:
        arbitrary_types_allowed = True
