import pika
import time
import redis
message="103,success"
timestamp=time.time()
pushToWriterProcessorQueue(message)

updateRedis(timestamp,message)

def pushToWriterProcessorQueue(message):
    credentials = pika.PlainCredentials(username='temp', password='temp')
    mqIp = "10.138.15.202"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='processor')
    channel.exchange_declare(exchange= 'events',exchange_type="direct")
    channel.queue_bind(exchange='events',queue="processor")
    channel.basic_publish(exchange='events', routing_key='processor', body=message)


def updateRedis(timestamp,message):
    redisIp= "10.138.15.204"
    redisEvents = redis.Redis(host=redisIp, db=1)
    redisEvents.set(timestamp,message)
