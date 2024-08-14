# PPTGen: PowerPoint Generation Tool

PPTGen is a Python tool for generating PowerPoint presentations based on CSV data.

## Installation

1. Ensure you have Python 3.7+ and Poetry installed on your system.

2. Clone the repository:
   ```bash
   git clone https://github.com/edpowers/pptx_autogen.git
   cd pptgen
   ```

3. Install the project dependencies using Poetry:
   ```bash
   poetry install
   ```

4. (Optional) Set up pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

## Usage

The main functionality of PPTGen is provided by the `generate_ppt` function in the `pptgen.entrypoint` module. Here's an example of how to use it:

```python
from pathlib import Path
from pptgen.entrypoint import generate_ppt

# Define your parameters
company_name = "ACME Corporation"
subtitle_company = "Annual Financial Report 2024"
csv_data_path = Path("/path/to/your/data.csv")
output_file = Path("/path/to/output/presentation.pptx")

# Generate the PowerPoint presentation
result_path = generate_ppt(
    company_name=company_name,
    subtitle_company=subtitle_company,
    csv_data_path=csv_data_path,
    output_file=output_file
)

print(f"PowerPoint presentation generated at: {result_path}")
```

This script will generate a PowerPoint presentation based on the provided CSV data and save it to the specified output file.

## Function Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `company_name` | str | The name of the company to be displayed in the presentation. |
| `subtitle_company` | str | A subtitle or additional information about the company. |
| `csv_data_path` | Path | The path to the CSV file containing the data for the presentation. |
| `output_file` | Path | The desired path and filename for the output PowerPoint file. |

## Development

To contribute to PPTGen:

1. Fork the repository on GitHub.
2. Clone your fork locally.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with clear, concise commit messages.
5. Push your changes to your fork on GitHub.
6. Create a pull request from your fork to the main repository.

Please ensure that your code follows the project's coding standards and includes appropriate tests.

## License

[MIT]
