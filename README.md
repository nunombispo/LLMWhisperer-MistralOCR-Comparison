# LLMWhisperer vs MistralOCR

A project to compare and demonstrate OCR (Optical Character Recognition) capabilities between LLMWhisperer and Mistral AI's OCR API.

## Overview

This project contains Python scripts that demonstrate how to use both LLMWhisperer and Mistral AI's OCR API to extract text from PDF documents. The scripts take a PDF file as input and process it through different OCR services for comparison purposes.

## Features

- **LLMWhisperer Integration**: Direct file processing with LLMWhisperer API
- **Mistral OCR Integration**: PDF to base64 encoding and processing with Mistral AI OCR API
- **Error handling** for file operations and API calls
- **Environment variable configuration** for API key management

## Prerequisites

- Python 3.7 or higher
- A Mistral AI API key
- A LLMWhisperer API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd LLMWhisperer-MistralOCR-Comparison
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root:

   ```
   MISTRAL_API_KEY=your_mistral_api_key_here
   LLMWHISPERER_API_KEY=your_llmwhisperer_api_key_here
   ```

2. Replace the API keys with your actual keys:

   **To get a Mistral AI API key:**

   - Visit [Mistral AI Console](https://console.mistral.ai/)
   - Sign up or log in to your account
   - Navigate to the API keys section
   - Generate a new API key
   - Copy the key and paste it in your `.env` file

   **To get a LLMWhisperer API key:**

   - Visit [LLMWhisperer](https://llmwhisperer.unstract.com/)
   - Sign up or log in to your account
   - Navigate to the API keys section
   - Generate a new API key
   - Copy the key and paste it in your `.env` file

## Usage

### Using Mistral OCR

Run the Mistral OCR script with a PDF file as an argument:

```bash
python mistral_ocr_example.py files/apple-finance.pdf
```

### Using LLMWhisperer

Run the LLMWhisperer script with a PDF file as an argument:

```bash
python llmwhisperer_example.py files/apple-finance.pdf
```

### Command Line Arguments

- `pdf_path`: Path to the PDF file you want to OCR (required)

## Project Structure

```
LLMWhisperer-MistralOCR-Comparison/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── mistral_ocr_example.py   # Mistral OCR script
├── llmwhisperer_example.py  # LLMWhisperer script
├── .env                     # Environment variables (create this)
└── files/                   # Sample PDF files
```

## Dependencies

The project uses the following Python packages:

- `mistralai`: Official Mistral AI Python client
- `llmwhisperer-client`: LLMWhisperer Python client
- `python-dotenv`: Environment variable management
- `base64`: Built-in Python module for base64 encoding

## API Documentation

For more information about the OCR APIs:

**Mistral AI:**

- [OCR API Reference](https://docs.mistral.ai/capabilities/OCR/document_ai_overview/)

**LLMWhisperer:**

- [LLMWhisperer API Reference](https://docs.unstract.com/llmwhisperer)
