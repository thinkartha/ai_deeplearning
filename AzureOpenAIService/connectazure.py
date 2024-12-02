import openai

# Set Azure OpenAI credentials
openai.api_type = "azure"
openai.api_base = "https://<your-resource-name>.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "<your-api-key>"

# Call GPT-4 model for text generation
response = openai.ChatCompletion.create(
    engine="gpt-4",  # Replace with your deployed model's name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain machine learning in simple terms."}
    ],
    max_tokens=100,
    temperature=0.7
)

# Print the response
print("Response:")
print(response['choices'][0]['message']['content'])
