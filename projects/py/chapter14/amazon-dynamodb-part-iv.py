from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
response = dynamodb.Table('reminder').query(
  KeyConditionExpression=Key('timestamp').eq(1511647270)
)
pprint(response['Items'])
## [{u'text': u'batch write example',
##    u'timestamp': Decimal('1511647270'),
##    u'ttl': Decimal('1511733670'),
##    u'userID': u'geish@voicera.ai'},
##  {u'text': u'another user',
##    u'timestamp': Decimal('1511647270'),
##    u'ttl': Decimal('1511733670'),
##    u'userID': u'user@example.com'}]
