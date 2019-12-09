import pika
import mysql.connector
import random
import time
input = 3


def pushToWriterProcessorQueue(message):
    credentials = pika.PlainCredentials(username='temp', password='temp')
    mqIp = "10.138.15.202"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='inputToWriteProcessor')
    channel.exchange_declare(exchange= 'events',exchange_type="direct")
    channel.queue_bind(exchange='events',queue="inputToWriteProcessor")
    channel.basic_publish(exchange='events', routing_key='inputToWriteProcessor', body=message)


def generateLogsAndPush(input):
    for i in range(input):
        id = random.randint(0,1000000)
        message = str(time.time())+';'+str(id)+','+'start'
        pushToWriterProcessorQueue(message)
        print(message)
        message = str(time.time())+';'+str(id)+','+'finish'
        if random.randint(0,1000000)%2 == 0:
            print(message)
            pushToWriterProcessorQueue(message)

generateLogsAndPush(input)
