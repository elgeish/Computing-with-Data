import boto3

dynamodb = boto3.resource('dynamodb')
with dynamodb.Table('reminder').batch_writer() as batch:
	batch.put_item(
		Item={
			'timestamp': 1511647270,
			'userID': 'geish@voicera.ai',
			'ttl': 1511733670,
			'text': 'batch write example',
		}
	)
	batch.put_item(
		Item={
			'timestamp': 1511647270,
			'userID': '@voicera.ai',
			'ttl': 1511733670,
			'text': 'batch write example',
		}
	)	
	batch.put_item(
		Item={
			'timestamp': 1511650870,
			'userID': 'geish@voicera.ai',
			'ttl': 1511737270,
			'text': 'another item to write',
		}
	)
	batch.delete_item(
		Key={
			'timestamp': 1511643670,
			'userID': 'geish@voicera.ai',
		}
	)
