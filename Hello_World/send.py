#Producer

import pika

#step1 --> create Connection witrh rabbit mq server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#step2 --> create queue to publish messages to
channel.queue_declare(queue='hello')

# A message can never be sent directly to the queue
# It always need to go through an exchange
# Default exchange = ''

#Step3 --> Publish( Sending Message)
channel.basic_publish(	exchange='',
						routing_key='hello',
						body='Hello World!')

print "[x] Sent Hello World!"

#Step4 --> Flush Network Buffers
connection.close()