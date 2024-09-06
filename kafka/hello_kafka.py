from confluent_kafka import Producer
import socket
# from fastapi import FastAPI

# app = FastAPI()

# Define the key variable
key = "some_key_value"

# Configuration for Kafka producer
conf = {'bootstrap.servers': "localhost:9092"}

# Create a producer instance
producer = Producer(conf)

producer.produce('my-topic', key=key, value=key)
producer.flush()  # Ensure the message is sent before exiting
print("Conectado al tópico 'my-topic' en Kafka!")

