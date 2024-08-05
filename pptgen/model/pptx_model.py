"""Powerpoint model."""

from pathlib import Path

from io import BytesIO

from pydantic import computed_field


from pptgen.model.base_paths import BasePaths


class PPTXModel(BasePaths):
    """Powerpoint model."""

    file_name: str
    pptx: BytesIO

    @computed_field
    @property
    def pptx_file(self) -> Path:
        """Get pptx file."""
        return self.output_path.joinpath(self.file_name).with_suffix(".pptx")

    def write_pptx(self) -> None:
        """Write pptx."""
        # Save the file
        with open(str(self.pptx_file), "wb") as f:
            f.write(self.pptx.getvalue())
