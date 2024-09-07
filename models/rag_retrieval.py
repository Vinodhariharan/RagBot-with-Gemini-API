from utils.vector_storage import get_embeddings
import clickhouse_connect

client = clickhouse_connect.get_client(
    host='host_address',
    port=443,
    username='username',
    password='password'
)

def get_relevant_docs(user_query):
    # Get the query embeddings
    query_embeddings = get_embeddings(user_query)
    
    # Convert the query embeddings to a suitable format for the query (JSON string)
    query_embeddings_str = ','.join(map(str, query_embeddings))

    # Make the query to the vector database
    query = f"""
        SELECT page_content,
               distance(embeddings, [{query_embeddings_str}]) as dist
        FROM default.handbook
        ORDER BY dist
        LIMIT 3
    """

    try:
        results = client.query(query)
        relevant_docs = [row['page_content'] for row in results.named_results()]
    except Exception as e:
        print(f"An error occurred: {e}")
        relevant_docs = []

    return relevant_docs



