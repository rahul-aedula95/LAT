import pika
import mysql.connector

mqIp = "10.138.15.202"
credentials = pia.PlainCredentials(username='temp', password='temp')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='processor')
channel.exchange_declare(exchange= 'events',exchange_type="direct")
channel.queue_bind(exchange='events',queue="processor")


def writeToView(message):
    #connection to db
    dbIp="10.138.15.211"
    #dbIp="localhost"
    mydb = mysql.connector.connect(host=dbIp,database="startMetrics",user='readprocessor1',password='Pass_123')

    mycursor = mydb.cursor()


    sql = "INSERT INTO start VALUES (%s, %s)"
    val = (message.split(',')[0], message.split(',')[1])

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode("utf-8") )
    if body.decode("utf-8").split(',')[1] =='start':
        writeToView(body.decode("utf-8") )

channel.basic_consume(
    queue='processor', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
