# ai_deeplearning
This is for any one in org to contribute their learnings for ai

For AWS Bedrock

Setup:

Install boto3: pip install boto3
Configure AWS credentials: aws configure
Replace "your-model-id" with the specific model ID from the list_foundation_models() output.


For Kafka set following configuration
```
KAFKA_URI = "address:port"
KAFKA_TOPIC_SOURCE = "source_topic"
KAFKA_TOPIC_SINK = "sink_topic"
KAFKA_CONSUMER_CLIENT_ID = "stockdata-client"
KAFKA_CONSUMER_GROUP_ID = "stockdata-group"
KAFKA_SSL_CA = "ca.pem"
KAFKA_SSL_CERT = "service.cert"
KAFKA_SSL_KEY = "service.key"
KAFKA_SECURITY_PROTOCOL = "SSL"
KAFKA_TIMEOUT = 1000
WAIT_TIME = 5
```

for Azure

```
Replace placeholders:
<your-resource-name>: Your Azure OpenAI resource name.
<your-api-key>: Your API key from the Azure portal.
Ensure the model (e.g., gpt-4) is deployed in your Azure OpenAI Service.
Use engine to specify the deployed model (e.g., gpt-4, gpt-3.5-turbo).
```

