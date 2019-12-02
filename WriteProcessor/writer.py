import pika
import time
import redis
import mysql.connector

message="103,success"
timestamp=time.time()
#pushToWriterProcessorQueue(message)

#updateRedis(timestamp,message)

def pushToReadProcessorQueue(message):
    credentials = pika.PlainCredentials(username='temp', password='temp')
    mqIp = "10.138.15.202"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='processor')
    channel.exchange_declare(exchange= 'events',exchange_type="direct")
    channel.queue_bind(exchange='events',queue="processor")
    channel.basic_publish(exchange='events', routing_key='processor', body=message)

def pushToReadProcessorQueueForFailures(message):
    credentials = pika.PlainCredentials(username='temp', password='temp')
    mqIp = "10.138.15.202"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='processorFailure')
    channel.exchange_declare(exchange= 'events',exchange_type="direct")
    channel.queue_bind(exchange='events',queue="processorFailure")
    channel.basic_publish(exchange='events', routing_key='processorFailure', body=message)


def updateRedis(timestamp,message):
    redisIp= "10.138.15.204"
    redisEvents = redis.Redis(host=redisIp, db=1)
    redisEvents.set(timestamp,message)


mqIp = "10.138.15.202"
credentials = pika.PlainCredentials(username='temp', password='temp')

connection2 = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
channel2 = connection2.channel()
channel2.queue_declare(queue='inputToWriteProcessor')
channel2.exchange_declare(exchange= 'events',exchange_type="direct")
channel2.queue_bind(exchange='events',queue='inputToWriteProcessor')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8") )
    pushToReadProcessorQueue(body.decode("utf-8").split(';')[1])
    pushToReadProcessorQueueForFailures(body.decode("utf-8").split(';')[1])
    updateRedis(body.decode("utf-8").split(';')[0],body.decode("utf-8").split(';')[1])


channel2.basic_consume(
    queue='inputToWriteProcessor', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel2.start_consuming()
