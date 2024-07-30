from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

producer = Producer({'bootstrap.servers': 'localhost:9092'})

for i in range(10):
    producer.produce('test_topic', key=str(i), value=f"message {i}", callback=delivery_report)
    producer.poll(1)

producer.flush()
