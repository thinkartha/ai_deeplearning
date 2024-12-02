import boto3

# Initialize Bedrock client
client = boto3.client('bedrock', region_name='us-east-1')

# List available foundation models
response = client.list_foundation_models()

print("Available Foundation Models:")
for model in response.get('models', []):
    print(f"- {model['modelId']} ({model['providerName']})")

# Example: Invoke a foundation model (replace with your modelId)
model_id = "your-model-id"
payload = {
    "input": "Write a short poem about the ocean."
}

response = client.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=json.dumps(payload)
)

# Parse and display the response
result = json.loads(response['body'])
print("Model Response:", result)
