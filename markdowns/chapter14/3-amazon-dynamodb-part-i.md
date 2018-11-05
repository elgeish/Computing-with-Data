# Amazon DynamoDB - Part I

We created a table called `reminder` to store user-requested reminders for our
previous example of a reminder bot. Now we can execute the following code
to create reminders:

```python
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
```
