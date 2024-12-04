
# Text Summarization Project

## Description
This project provides a console-based tool for summarizing long texts into concise and meaningful summaries. It utilizes a pre-trained transformer model for generating high-quality summaries.

## Features
- Summarizes long texts into concise summaries.
- Configurable summary length (minimum and maximum).
- Easy-to-use console-based interface.

## Installation

### 1. Clone the Repository
Download or clone the repository to your local machine.

### 2. Setup Python Environment
Ensure you have Python 3.7+ installed. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate   # For Windows
```

### 3. Install Dependencies
Install the required libraries using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Script
Execute the script to start the summarization tool:

```bash
python text_summarization.py
```

### 2. Provide Input
Enter the text you want to summarize. The tool will process the text and return a summary.

### 3. Exit the Tool
Type `exit` to quit the tool.

## File Structure
- `text_summarization.py`: The main script for text summarization.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Specifies files and directories to ignore in version control.

## Future Enhancements
- Add support for multiple languages.
- Export summaries to PDF or HTML formats.
- Integrate with a web or mobile interface.

## Requirements
- Python 3.7+
- Transformers library
