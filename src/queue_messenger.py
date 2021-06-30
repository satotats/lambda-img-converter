import logging
import boto3
import json
from botocore.exceptions import ClientError

def send(queue_name, bucket_name, file_name):
    sqs = boto3.resource('sqs')

    try:	
        queue = sqs.get_queue_by_name(QueueName=queue_name)
    except ClientError as e:	
        logging.error(e)
        
    message = json.dumps({'bucket': bucket_name, 'file_name': file_name})
    queue.send_message(MessageBody=message)
