import pika
import mysql.connector

mqIp = "10.138.15.202"
credentials = pika.PlainCredentials(username='temp', password='temp')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='processorFailure')
channel.exchange_declare(exchange= 'events',exchange_type="direct")
channel.queue_bind(exchange='events',queue="processorFailure")


def writeToView(message):
    #connection to db
    dbIp="10.138.15.205"
    #dbIp="localhost"
    mydb = mysql.connector.connect(host=dbIp,database="failureMetrics",user='readprocessor2',password='Pass_123')

    mycursor = mydb.cursor()


    sql = "INSERT INTO failure VALUES (%s, %s)"
    val = (message.split(',')[0], message.split(',')[1])

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8") )
    if body.decode("utf-8").split(',')[1] =='failure':
        writeToView(body.decode("utf-8") )

channel.basic_consume(
    queue='processorFailure', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
