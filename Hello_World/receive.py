#Consumer

import pika

#step1 --> create Connection witrh rabbit mq server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#step2 --> create queue to subscribe messages from 
# Yes create just in case its not already there
# Creating a queue is idempotent

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

#step3 --> Subscribe(recieve messages)

#Need to subscribe to a callback function of a queue
#Callback function initiated once we start receiveing messages

def callback(ch,method,properties,body):
	print "[x] Received %r" % (body,)

#consumption
channel.basic_consume(	callback,
						queue='hello',
						no_ack=True)

#step4 --> Never ending loop of consumption bwahahaha

channel.start_consuming()