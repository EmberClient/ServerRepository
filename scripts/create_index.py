from jsonschema import validate
from json import load, dump
from os import listdir

# Load the schema
schema = load(open('server.schema.json'))

# Create an empty array to store the index
index = []

# Read the files in the directory
for server in listdir('servers'):
    print('Validating %s...' % server, end = ' ')

    # Open the file and load the JSON
    with open('servers/%s' % server) as f:
      try:
        serverJson = load(f)

        # Validate the JSON
        validate(serverJson, schema)

        # Add the server to the index
        index.append(serverJson)

        print('OK')
      except Exception as e:
        print('FAILED')

# Save the index
print('Saving index...', end = ' ')
try:
  with open('index.json', 'w') as f:
    dump(index, f)
  print('OK')
except Exception as e:
  print('FAILED')