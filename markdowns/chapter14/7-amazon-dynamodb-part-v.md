# Amazon DynamoDB - Part V

To get all reminders that belong to a specific user, we scan the table using
the following attribute condition:

```python
from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
response = dynamodb.Table('reminder').scan(
  FilterExpression=Attr('userID').eq('geish@voicera.ai')
)
pprint(response['Items'])
## [{u'text': u'batch write example',
##    u'timestamp': Decimal('1511647270'),
##    u'ttl': Decimal('1511733670'),
##    u'userID': u'geish@voicera.ai'},
##  {u'text': u'another item to write',
##    u'timestamp': Decimal('1511650870'),
##    u'ttl': Decimal('1511737270'),
##    u'userID': u'geish@voicera.ai'}]
```
