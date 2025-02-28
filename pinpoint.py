import boto3
import json

pinpoint = boto3.client('pinpoint')

def lambda_handler(event, context):
    x=json.loads(event["body"])
    print(x["answer"])
    pinpoint.send_messages(
        ApplicationId='6712ad2c***********688975d992ef',
        MessageRequest={
            'Addresses' : {
                "+346*******5" : {'ChannelType': 'SMS'}
            },
            'MessageConfiguration' : {
                'SMSMessage' : {
                    'Body': x["answer"],
                    'MessageType': 'PROMOTIONAL'
                }
            }
        }
    )
    return {
        'statusCode': 200,
        'body': x["answer"]
    }