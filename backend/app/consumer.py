import pika
import os
from database import DBMongo
import time
import json


class Rabbit:
    def __init__(self) -> None:
        host = "rabbitmq"
        rabbit_user = os.environ.get("RABBITMQ_DEFAULT_USER")
        rabbit_pass = os.environ.get("RABBITMQ_DEFAULT_PASS")
        amqp_port = os.environ.get("RABBITMQ_AMQP_PORT")
        credentials = pika.PlainCredentials(rabbit_user,
                                            rabbit_pass)
        params = pika.ConnectionParameters(host,
                                        amqp_port,
                                        "/",
                                        credentials)
        conn = pika.BlockingConnection(params)
        self.channel = conn.channel()

    def consume_data(self):
        rabbit_q = os.environ.get("RABBITMQ_QUEUE")
        channel = self.channel
        channel.queue_declare(queue=rabbit_q, durable=True)
        method_frame, header_frame, body = channel.basic_get(rabbit_q, auto_ack = True)
        return body


def to_mongo():
    WAIT_AFTER_CONSUME = os.environ.get("WAIT_AFTER_CONSUME")
    rabbit = Rabbit()
    mongo = DBMongo()
    MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")
    while True:
        data = rabbit.consume_data()
        database = mongo.get_db()
        if data is None:
            continue
        q_data = json.loads(data)
        exist_data = list(database[MONGO_COLLECTION].find({"entity_id":q_data["entity_id"]}))
        if exist_data != []:
            continue
        if data is not None:
            database[MONGO_COLLECTION].insert_one(q_data)
            time.sleep(float(WAIT_AFTER_CONSUME))
        else:
            time.sleep(15)

