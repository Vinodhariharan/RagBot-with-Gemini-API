import streamlit as st
from models.gemini_integration import query_gemini
from models.rag_retrieval import get_relevant_docs

def display_chat():
    st.title("Chat with Vector DB and Gemini")

    query = st.text_input("Enter your query:")

    if query:
        st.write("Fetching relevant docs from vector DB...")
        relevant_text = get_relevant_docs(query)
        
        st.write("Sending prompt to Gemini...")
        answer = query_gemini(query, relevant_text)
        
        st.write("Answer from Gemini:")
        st.write(answer)
