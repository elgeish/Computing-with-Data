import json

# creating a Python object (map) holding a person's address
personRecord = {
  "firstName": "Jane",
  "lastName": "Doe",
  "yearOfBirth": 1975,
  "address": {
    "streetAddress": "100 Main Street",
    "city": "Los Angeles",
    "state": "CA",
    "postalCode": "90021"
  },
  "phoneNumbers": [
    { "type": "home", "number": "(444) 555-1234" },
    { "type": "office",  "number": "(444) 555-1235" }
  ]
}

# convert the Python object into a JSON string
personRecordJSON = json.dumps(personRecord)
personRecordReconstructed = json.loads(personRecordJSON)

# print the firstName field of the reconstructed Python object
print(personRecordReconstructed['firstName'])
