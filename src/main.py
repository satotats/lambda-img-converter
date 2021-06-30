import s3_uploader as uploader
import queue_messenger as messenger
import logging

bucket_name = 'bucketname'
queue_name = 'queuename'

file_path = 'path-to\\sample.JPG'

path_parsed = file_path.split('\\') 
file_name = path_parsed[len(path_parsed)-1]

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s')

logging.debug('bucket_name name: ' + bucket_name+ ' queue_name: '+ queue_name +' file_path: '+ file_path)

uploader.upload_file(bucket_name, file_path, file_name)
messenger.send(queue_name, bucket_name, file_name)

logging.debug('end')