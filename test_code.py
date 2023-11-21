import mlflow
import boto3

mlflow.set_tracking_uri('http://ec2-35-180-111-0.eu-west-3.compute.amazonaws.com:5000/')

dictionary = {"k": "v"}

with mlflow.start_run():

    mlflow.log_param("alpha", 5)
    mlflow.log_param("l1_ratio", 89)
    mlflow.log_dict(dictionary, "data.json")

