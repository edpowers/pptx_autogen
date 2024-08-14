"""Base Model for the basic paths."""

from pathlib import Path

from pydantic import BaseModel, computed_field


def find_project_root(current_path: Path = Path.cwd()) -> Path:
    """
    Recursively search for a pyproject.toml file to determine the project root.

    Args:
    current_path (Path): The path to start searching from. Defaults to the current working directory.

    Returns:
    Path: The path containing the pyproject.toml file, or the root directory if not found.
    """
    if (current_path / "pyproject.toml").exists():
        return current_path

    parent_path = current_path.parent
    if parent_path == current_path:  # We've reached the root directory
        raise FileNotFoundError(
            "Could not find pyproject.toml in any parent directory."
        )

    return find_project_root(parent_path)


class BasePaths(BaseModel):
    """BaseModel for the basic paths."""

    @computed_field  # type: ignore
    @property
    def data_path(self) -> Path:
        """Data path."""
        return find_project_root().joinpath("data")

    @computed_field
    @property
    def output_path(self) -> Path:
        """Output path."""
        return self.data_path / "output"

    @computed_field
    @property
    def image_path(self) -> Path:
        """Image path."""
        return self.data_path / "images"

    def find_image(self, file_name: str) -> str:
        """Find the image path."""
        extensions = ["*.png", "*.jpg", "*.jpeg"]
        # Get the list of all files in the image directory
        image_files = [f for ext in extensions for f in self.image_path.rglob(ext)]

        if not image_files:
            raise FileNotFoundError("No images found in the image directory")

        # Find the file name in the list of files
        for image_file in image_files:
            if image_file.name == file_name or file_name in image_file.name:
                return str(image_file.resolve())

        raise FileNotFoundError(f"Could not find {file_name} in the image directory.")
