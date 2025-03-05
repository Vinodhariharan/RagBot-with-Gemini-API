import pandas as pd
import clickhouse_connect
import google.generativeai as genai
import os

# Setup Google Generative AI
google_api_key = 'AIzaSyAD4QZ-4djS3O7U85CtlldTBy0Vew0iAnA'  # Replace with your API key
genai.configure(api_key=google_api_key)

# Setup ClickHouse client
client = clickhouse_connect.get_client(
    host='host_address',
    port=443,
    username='username',
    password='password'
)

# Create the table if not exists
client.command("""
    CREATE TABLE IF NOT EXISTS default.handbook (
        id Int64,
        page_content String,
        embeddings Array(Float32),
        CONSTRAINT check_data_length CHECK length(embeddings) = 768
    ) ENGINE = MergeTree()
    ORDER BY id
""")

def upload_file_to_vector_db(dataframe):
    """
    Upload the DataFrame with page content and embeddings to the vector database.
    """
    batch_size = 10
    num_batches = len(dataframe) // batch_size + (1 if len(dataframe) % batch_size != 0 else 0)
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(dataframe))
        batch_data = dataframe.iloc[start_idx:end_idx]
        
        # Convert DataFrame to list of tuples
        batch_records = batch_data.to_records(index=False).tolist()
        
        # Insert the data into ClickHouse
        client.insert("default.handbook", batch_records, column_names=batch_data.columns.tolist())
        print(f"Batch {i+1}/{num_batches} inserted.")
    
    # Create or update a vector index for quick retrieval
    client.command("""
    ALTER TABLE default.handbook
        ADD VECTOR INDEX IF NOT EXISTS vector_index embeddings
        TYPE MSTG
    """)

def get_embeddings(text):
    """
    Generate embeddings for the provided text using the Google Generative AI API.
    """
    model = 'models/embedding-001'  # Replace with your model
    result = genai.embed_content(
        model=model,
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']
