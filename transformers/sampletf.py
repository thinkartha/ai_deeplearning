from transformers import pipeline

# Load a text generation model (e.g., GPT-2)
text_generator = pipeline("text-generation", model="gpt2")
print("Text Generation:")
print(text_generator("Once upon a time", max_length=50)[0]['generated_text'])

# Load a sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")
print("\nSentiment Analysis:")
print(sentiment_analyzer("I love working with AI models!"))

# Load a question-answering model
qa_model = pipeline("question-answering")
print("\nQuestion Answering:")
print(qa_model({
    "question": "What is the capital of France?",
    "context": "France's capital is Paris, known for its art and culture."
}))

# Load an image classification model
from PIL import Image
image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
image = Image.open("path/to/image.jpg")  # Replace with an image path
print("\nImage Classification:")
print(image_classifier(image))
