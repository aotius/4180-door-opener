import boto3
from selenium import webdriver
from boto3.dynamodb.conditions import Key, Attr

AWS_ACCESS_KEY = "____________"
# Add AWS IAM Access Key String Here
AWS_SECRET_ACCESS_KEY = "__________________"
# Add AWS IAM Access Secret Key String Here
AWS_REGION = "us-east-1"

# DynamoDB Table
DYNAMODB_TABLE = 'GTBuzzcards4180'

dynamodb = boto3.resource('dynamodb', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

table = dynamodb.Table(DYNAMODB_TABLE)

# Web access

driver = webdriver.Chrome()
# Need chromedriver in the file path
url = "http://192.168.137.41/"
# Add mbed wifi module website url here

def checkUser(id):
    items = table.scan(FilterExpression=Attr('gtID').eq(id))['Items']
    if len(items) == 0:
        return False
    else:
        return True
    return True

if __name__ == '__main__':
    while True:
        gtid = input('Swipe your Buzzcard:')
        confirmed = checkUser(gtid)
        if confirmed:
            driver.get(url)
            confirmed = False
