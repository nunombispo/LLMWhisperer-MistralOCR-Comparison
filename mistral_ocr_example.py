import base64
import os
import sys
from mistralai import Mistral
from dotenv import load_dotenv

# Load the environment variables
load_dotenv(".env")

# Function to encode the PDF to base64
def encode_pdf(pdf_path):
    """Encode the pdf to base64."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None


# Function to OCR the PDF
def ocr_pdf(base64_pdf):
    """OCR the pdf."""
    api_key = os.getenv("MISTRAL_API_KEY")
    client = Mistral(api_key=api_key)

    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": f"data:application/pdf;base64,{base64_pdf}" 
        },
        include_image_base64=True
    )

    # Return the OCR response
    return ocr_response


# Main function
if __name__ == "__main__":
    # Get the path to the PDF file from the command line
    pdf_path = sys.argv[1]

    # Getting the base64 string
    base64_pdf = encode_pdf(pdf_path)

    # OCR the PDF
    ocr_response = ocr_pdf(base64_pdf)

    # Print the OCR response
    print(ocr_response)
