
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import time
# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
        
def lambda_handler(event, context):
    
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    print(event)
    
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    print("found")
    table = dynamodb.Table('User')
    sns=boto3.client('sns')
    status = dynamodb.Table('CheckDevice')

    userlist=["C1","C2","C3"]
    #check for each user 
    for clientid in userlist:
        try:
            #from user table
            response = table.get_item(
                Key={
                    'clientid':clientid
                }
            )
            #from chechdevice table
            print(response)
            response_stat = status.get_item(
                Key={
                    'clientid':clientid
                }
            )
            print(response_stat)
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']
            stat_item=response_stat['Item']
            
            print("GetItem succeeded:")
            fitem=json.dumps(item, indent=4, cls=DecimalEncoder)
            fitem1 = json.loads(fitem)
            
            fitem_stat=json.dumps(stat_item, indent=4, cls=DecimalEncoder)
            fitem1_stat = json.loads(fitem_stat)
            
            
            print(fitem1["name"])
            print(fitem1_stat)
            
            
            
            response_update = table.update_item(
                Key={
                    'clientid':clientid
                },
                UpdateExpression="set flag = :r",
                ExpressionAttributeValues={
                    ':r': decimal.Decimal(0),
            
                },
                ReturnValues="UPDATED_NEW"
            )
            print(response_update)
            phone=fitem1["phone"]
            print(phone)
            
            #get timestamp
            timestamp=fitem1_stat["payload"]["payloadtimestamp"]
            print(timestamp)
            
            current_time=time.time()
            print(current_time)
            #find difference
            diff=current_time-timestamp
            print(diff)
            
            #if difference greater than 10 min then send message
            if(diff>600*1000):
                respo=sns.publish(PhoneNumber = phone, Message="Your Device is not Working", Subject="Device Health")
                print(respo)
    
    return 'Hello from Lambda'
