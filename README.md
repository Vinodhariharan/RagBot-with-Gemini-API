# RagBot with Gemini API

## Overview
RagBot is an AI-powered chatbot that integrates Retrieval-Augmented Generation (RAG) with Google's Gemini API. It retrieves relevant documents from a vector database and enhances responses using a generative AI model. This project is built using Streamlit for the frontend and ClickHouse for vector storage.

## Features
- Extracts and processes text from PDFs and images
- Converts text into vector embeddings for efficient search
- Retrieves relevant documents based on user queries
- Generates AI-powered responses using the Gemini API
- Built with Streamlit for an interactive UI

## Technologies Used
- **Python** (Streamlit, Pandas, PyPDF2)
- **Google Gemini API** for text generation
- **ClickHouse** for vector storage and retrieval
- **Google Generative AI** for content embedding
- **PyPDF2** for PDF text extraction
- **OpenCV & Tesseract OCR** for image processing

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Vinodhariharan/RagBot-with-Gemini-API.git
   ```
2. Navigate to the project directory:
   ```sh
   cd RagBot-with-Gemini-API
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - `GEMINI_API_KEY`: Your API key for the Gemini API
   - `CLICKHOUSE_HOST`, `CLICKHOUSE_USERNAME`, `CLICKHOUSE_PASSWORD`: ClickHouse database credentials

## Usage
1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
2. Upload a PDF or an image to extract and store content in the vector database.
3. Enter a query in the chatbot interface to retrieve relevant documents and get AI-generated responses.

## Project Structure
```
RagBot-with-Gemini-API/
│── app.py                    # Main Streamlit application
│── requirements.txt          # Python dependencies
│── utils/
│   │── vector_storage.py      # Vector DB operations
│   │── pdf_processing.py      # PDF text extraction
│   │── image_processing.py    # Image text extraction
│── models/
│   │── gemini_integration.py  # Gemini API integration
│   │── rag_retrieval.py       # Retrieval logic
│── pages/
│   │── chat.py                # Chat interface
│   │── upload.py              # Upload interface
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

