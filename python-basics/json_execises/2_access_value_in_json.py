# Access the value of key2 from the following JSON

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
value = data['key2']
print("value")