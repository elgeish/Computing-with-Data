from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('reminder')
with table.batch_writer() as batch:
  batch.put_item(
    Item={
      'timestamp': 1511652070,
      'userID': 'checklist@example.com',
      'ttl': 1511738470,
      'checklist': ['milk', 'eggs', 'bread']
    }
  )
  batch.put_item(
    Item={
      'timestamp': 1511652070,
      'userID': 'complex@example.com',
      'ttl': 1511738470,
      'actions': [{
        'callback': 'example.com/callback',
        'payload': {'text': 'flash office lights'},
        'method': 'POST'
      }]
    }
  )

response = table.query(
  KeyConditionExpression=Key('timestamp').eq(1511652070)
)
pprint(response['Items'])
## [{u'checklist': [u'milk', u'eggs', u'bread'],
##   u'timestamp': Decimal('1511652070'),
##   u'ttl': Decimal('1511738470'),
##   u'userID': u'checklist@example.com'},
## {u'actions': [{u'callback': u'example.com/callback',
##     u'method': u'POST',
##     u'payload': {u'text': u'flash office lights'}}],
##   u'timestamp': Decimal('1511652070'),
##   u'ttl': Decimal('1511738470'),
##   u'userID': u'complex@example.com'}]
