from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9092",
    client_id='hola_mundo_kafka'
)

topic_list = [NewTopic(name="hola_mundo_topic", num_partitions=1, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)

print("Hola Mundo desde Kafka! Tópico creado.")
