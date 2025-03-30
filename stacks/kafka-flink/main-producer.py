from fastapi import FastAPI
from pydantic import BaseModel
from confluent_kafka import Producer
import json

app = FastAPI()

# Kafka producer configuration
producer = Producer({
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'security.protocol': 'PLAINTEXT',  # Ensure it is PLAINTEXT if you're not using SSL
})

# Kafka producer callback
def delivery_callback(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Define a Pydantic model for the request body
class MessageRequest(BaseModel):
    message: str

@app.post("/send_message")
async def send_message(message_request: MessageRequest):
    message = message_request.message
    # Produce a message to Kafka topic
    producer.produce('my_topic', value=json.dumps(message), callback=delivery_callback)
    producer.flush()
    return {"message": "Message sent to Kafka!"}
