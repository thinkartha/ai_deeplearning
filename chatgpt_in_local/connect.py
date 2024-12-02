import openai

# Set your OpenAI API key
openai.api_key = "your-api-key"

# ChatGPT interaction
response = openai.ChatCompletion.create(
    model="gpt-4",  # Use "gpt-3.5-turbo" if needed
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain how to set up ChatGPT locally in Python."}
    ],
    temperature=0.7,
    max_tokens=150
)

# Print the response
print("ChatGPT Response:")
print(response['choices'][0]['message']['content'])
