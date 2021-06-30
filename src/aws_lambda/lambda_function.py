import boto3
import json
from PIL import Image
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(asctime)s: %(message)s")

def lambda_handler(event, context):
    logging.debug("start conversion")
    s3_client = boto3.client("s3")

    for record in event["Records"]:	
        body = json.loads(str(record["body"]))	
        bucket = body["bucket"]	
        old_filename = body["file_name"]	

        download_path = "/tmp/downloads"
        s3_client.download_file(bucket, old_filename, download_path)
        img = Image.open(download_path)

        new_filename = "resized_" + old_filename
        uploaded_file_path = "/tmp/" + new_filename
        img.resize((img.width // 2, img.height // 2)).save(uploaded_file_path)

        s3_client.upload_file(uploaded_file_path, bucket, new_filename)

        # NOTE: 
        # s3.download_file は フォルダが無い場合はフォルダを作成するが
        # Image.save はフォルダが無い場合にはエラーとなる(作成してくれない)
    
