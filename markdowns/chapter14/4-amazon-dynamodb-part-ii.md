# Amazon DynamoDB - Part II

To get that item we just created, we simply can query for it:

```python
from pprint import pprint

import boto3

dynamodb = boto3.resource('dynamodb')
response = dynamodb.Table('reminder').get_item(
	Key={
	'timestamp': 1511643670,
	'userID': 'geish@voicera.ai',
	}
)
pprint(response['Item'])
## {u'text': u'write a DynamoDB example',
## 	u'timestamp': Decimal('1511643670'),
## 	u'ttl': Decimal('1511730070'),
## 	u'userID': u'geish@voicera.ai'}
```
