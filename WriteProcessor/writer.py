import pika
credentials = pika.PlainCredentials(username='temp', password='temp')
mqIp="10.138.15.202"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=mqIp,credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='processor')
channel.exchange_declare(exchange= 'events',exchange_type="direct")
channel.queue_bind(exchange='events',queue="processor")
message="103,success"
channel.basic_publish(exchange='events', routing_key='processor', body=message)
