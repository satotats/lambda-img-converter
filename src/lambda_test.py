import aws_lambda.lambda_function as lambda_f

message = {
  "Records": [
    {
      "body": '{"bucket": "satotats-bucket1", "file_name": "hello"}',
    }
  ]
}

lambda_f.lambda_handler(message, None)
