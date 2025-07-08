import os
from dotenv import load_dotenv
from unstract.llmwhisperer import LLMWhispererClientV2  
from unstract.llmwhisperer.client_v2 import LLMWhispererClientException  
import sys  
  
# Load the API key from the .env file
load_dotenv()

# Function to process a document  
def process_document(file_path):  
    # Initialize the client with your API key  
    client = LLMWhispererClientV2(base_url="https://llmwhisperer-api.us-central.unstract.com/api/v2",  
                                  api_key=os.getenv("LLMWHISPERER_API_KEY"))  
    # Call the sync method with the file path  
    try:  
        result = client.whisper(  
            file_path=file_path,  
            wait_for_completion=True,  
            wait_timeout=200,  
        )  
        return result['extraction']['result_text']  
    except LLMWhispererClientException as e:  
        print(e)  
        return None

# Main  function  
if __name__ == "__main__":  
    # Get the path to the PDF file from the command line
    pdf_path = sys.argv[1]

    # Call the function to process the document
    result = process_document(pdf_path)

    # Print the result
    print(result)
