from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    hosts=["http://localhost:9200"],  # Update with your ES host
    basic_auth=("username", "password")  # Add credentials if required
)

# Create an index
index_name = "my-index"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"Index '{index_name}' created.")

# Index a document
doc = {
    "title": "AI in Elasticsearch",
    "content": "Using AI with Elasticsearch is powerful!",
    "timestamp": "2024-12-02"
}
response = es.index(index=index_name, document=doc)
print(f"Document indexed: {response['_id']}")

# Search documents
query = {
    "query": {
        "match": {
            "content": "AI"
        }
    }
}
response = es.search(index=index_name, body=query)
print("Search Results:")
for hit in response['hits']['hits']:
    print(hit['_source'])

# Delete the index
es.indices.delete(index=index_name, ignore=[400, 404])
print(f"Index '{index_name}' deleted.")
