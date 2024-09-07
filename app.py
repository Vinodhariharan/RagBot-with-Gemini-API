import streamlit as st

st.set_page_config(page_title="Vector Chat App", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Chat", "Upload"])

if page == "Chat":
    from pages import chat
    chat.display_chat()
elif page == "Upload":
    from pages import upload
    upload.display_upload()
