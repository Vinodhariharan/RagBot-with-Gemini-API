import google.generativeai as genai

google_api_key='your_api_key'  # Pass API key directly
genai.configure(api_key=google_api_key)

def query_gemini(query, relevant_text):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    relevant_passage = " ".join(relevant_text)
    response = model.generate_content(
        f"You are a helpful and informative chatbot that answers questions using text from the reference passage included below. "
        f"Respond in a complete sentence and make sure that your response is detailed and easy to understand for everyone. "
        f"Maintain a friendly and conversational tone. If the passage is irrelevant, feel free to ignore it.\n\n"
        f"QUESTION: '{query}'\n"
        f"UPLOADED DOC INFO: '{relevant_passage}'\n\n"
        f"ANSWER:"
    )

    return response.text