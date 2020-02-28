import json
import base64
import boto3

def lambda_handler(event,context)
  s3= boto3.client("s3")
  bucketname=event["params"]["path"]["bucket"]
  file_name=event["params"]["querystring"]["file"]
  file_obj=s3.get_object(Bucket=bucketname,Key=file_name)
  file_content=fileobj["Body"].read()
  URL=s3.generate_presigned_url("get_object",
    Params={"Bucket":bucketname,"Key":file_name},ExpiredIn=100)
  print(bucketname,file_name)
  return {
      "statuscode":"200",
      "headers": {"Content-Type":"application/json"},
      "body": json.dumps("URL",URL),
      "isBase64Encoded": False

  }
