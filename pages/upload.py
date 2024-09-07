import streamlit as st
import pandas as pd
from utils.vector_storage import upload_file_to_vector_db, get_embeddings
from utils.pdf_processing import extract_text_from_pdf
from utils.image_processing import process_image

def display_upload():
    st.title("Upload Files to Vector DB")

    uploaded_file = st.file_uploader("Upload a PDF or Image", type=["pdf", "jpg", "png"])
    
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            page_texts = extract_text_from_pdf(uploaded_file)
            st.write("Extracted text from PDF:")
            st.write(page_texts)
        else:
            text = process_image(uploaded_file)
            st.write("Extracted content from Image:")
            st.write(text)
            page_texts = [text]  # Treat image content as a single page

        # Prepare a dataframe for each page content
        data = {'page_content': [], 'embeddings': []}
        
        for page_text in page_texts:
            st.write("Generating embeddings for a page...")
            embeddings = get_embeddings(page_text)
            data['page_content'].append(page_text)
            data['embeddings'].append(embeddings)
        
        dataframe = pd.DataFrame(data)
        
        # Upload the file content and embeddings to the vector database
        st.write("Uploading to Vector DB...")
        upload_file_to_vector_db(dataframe)
        st.success("File successfully uploaded to vector database.")

        st.write("Uploaded data:")
        st.write(dataframe)
