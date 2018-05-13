
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

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
    #create boto3 client
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    
    print(event['clientid'])
    clientid=event['clientid']
    dynamodb = boto3.resource("dynamodb", region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")

    table = dynamodb.Table('User')
    #sns client
    sns=boto3.client('sns')
    #get information about the client whose id is given 
    try:
        response = table.get_item(
            Key={
                'clientid':clientid
            }
        )
        print(response)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        
        print("GetItem succeeded:")
        fitem=json.dumps(item, indent=4, cls=DecimalEncoder)
        fitem1 = json.loads(fitem)
        print(fitem1["name"])
        #set flag of the client
        if(fitem1['flag']==0):
            response_update = table.update_item(
                Key={
                    'clientid':clientid
                },
                UpdateExpression="set flag = :r",
                ExpressionAttributeValues={
                    ':r': decimal.Decimal(1),
        
                },
                ReturnValues="UPDATED_NEW"
            )
            print(response_update)
            phone=fitem1["phone"]
            
            #send alert message
            if(event['bp']<90):
                respo=sns.publish(PhoneNumber = phone, Message="Your BP is low", Subject="BP Alert")
                print(respo)
            if(event['bp']>140):
                respo=sns.publish(PhoneNumber = phone, Message="Your BP is high", Subject="BP Alert")
                print(respo)
                
        else:
            print("flag set not sending message")
            
    return 'Hello from Lambda'
