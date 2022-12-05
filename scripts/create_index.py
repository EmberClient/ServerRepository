from jsonschema import validate
from json import load, dump
from os import listdir

# Load the schema
schema = load(open('server.schema.json'))

def get_servers():
  servers = {}

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
          servers[server] = serverJson

          print('OK')
        except Exception:
          print('FAILED')

          # Something went wrong, we'll throw an exception
          raise ValueError('Invalid server file: %s' % server)
  
  return servers

if __name__ == '__main__':
  # Get the validated servers
  servers = get_servers()

  # Save the index
  print('Saving index...', end = ' ')
  try:
    with open('servers.json', 'w') as f:
      dump(servers, f)
    print('OK')
  except Exception as e:
    print('FAILED')
    raise e
