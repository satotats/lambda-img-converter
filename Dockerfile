FROM amazonlinux:latest

RUN amazon-linux-extras install -y python3.8
RUN mkdir /home/aws_lambda