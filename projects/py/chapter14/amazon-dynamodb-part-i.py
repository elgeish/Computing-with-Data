import boto3

dynamodb = boto3.resource('dynamodb')
dynamodb.Table('reminder').put_item(
  Item={
    'timestamp': 1511643670,
    'userID': 'geish@voicera.ai',
    'ttl': 1511730070,
    'text': 'write a DynamoDB example',
  }
)
