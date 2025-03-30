import uuid

from fastapi import FastAPI
from confluent_kafka import Consumer, KafkaException

app = FastAPI()

# Kafka consumer configuration
unique_group_id = f"consumer_group_{uuid.uuid4()}"

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': unique_group_id,
    'auto.offset.reset': 'earliest',
})

# Subscribe to a topic
consumer.subscribe(['my_topic'])

@app.on_event("startup")
async def start_consumer():
    print(f"Starting consumer with group ID: {unique_group_id}")
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue  # No message
        if msg.error():
            raise KafkaException(msg.error())
        print(f"Received message: {msg.value().decode('utf-8')}")


@app.on_event("shutdown")
def stop_consumer():
    consumer.close()
