import pika
import mysql.connector

mqIp = localhost
connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp))
channel = connection.channel()
channel.queue_declare(queue='processor')
channel.exchange_declare(exchange= 'events',exchange_type="direct")
channel.queue_bind(exchange='events',queue="processor")

def writeToView(message):
    #connection to db
    dbIp="35.247.114.246"
    mydb = mysql.connector.connect(host=dbIp,database="successMetrics",user='newuser',password='password',port=3306)

    mycursor = mydb.cursor()


    sql = "INSERT INTO status VALUES (%s, %s)"
    val = (message.split(',')[0], message.split(',')[1])
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    writeToView(body)

channel.basic_consume(
    queue='processor', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
