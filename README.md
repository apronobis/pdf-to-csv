# PDF Processing Script

This project processes a PDF file to extract tables, crop images, and save the processed data to a CSV file.

## Runtime Environment

This project requires the following components to be installed in your runtime environment:

- **Python**: Ensure Python is installed from [Python’s official website](https://www.python.org/downloads/). 
- **Java Runtime Environment (JRE)**: Required for the Tabula Python library, which extracts tables from PDFs.
   - **Windows**: You can download jre installer from [Oracle's website](https://www.oracle.com/java/technologies/downloads/).
   - **Ubuntu/Debian**: `sudo apt-get install default-jre`
- **Poppler**: A PDF rendering library used for converting PDFs to images.
   - **Windows**: Download the Poppler binaries from the [Poppler for Windows page](https://github.com/oschwartz10612/poppler-windows/releases) and add the `bin` directory to your system `PATH`.
   - **Ubuntu/Debian**: `sudo apt-get install poppler-utils`
- **AWS CLI**: Install following the official guide from [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## Verification

After installing the required components, verify the setup with the following commands:

- **JRE**: `java -version`
- **Poppler**: `pdftotext -v`
- **AWS CLI**: `aws --version`
- **Python**: `python --version` or `python3 --version`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/apronobis/pdf-to-excel.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd pdf-to-excel
    ```
3. **Install Python dependencies**:
    Ensure you have `pip` installed, then run:
    ```bash
    pip install -r requirements.txt
    ```
4. **Verify runtime environment**:
    ```bash
    java -v
    pdftoppm -v
    aws --version
    ```

## Usage

To parse the Request PDF, run:

```bash
python extract.py
```

The result will be saved as a CSV file in the output folder.