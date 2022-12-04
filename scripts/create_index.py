from jsonschema import validate
from json import load, dump
from os import listdir

# Load the schema
schema = load(open('server.schema.json'))

def get_valid_servers():
  validated_servers = []

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
          validated_servers.append(serverJson)

          print('OK')
        except Exception as e:
          print('FAILED')
          print(e)

          exit(1)
  
  return validated_servers

if __name__ == '__main__':
  # Save the index
  print('Saving index...', end = ' ')
  try:
    with open('index.json', 'w') as f:
      dump(get_valid_servers(), f)
    print('OK')
  except Exception as e:
    print('FAILED')
    print(e)

    exit(1)