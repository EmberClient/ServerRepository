from jsonschema import validate
from json import load, dump
from os import listdir
import os

def load_json(file_path):
    """Load a JSON file from the given path."""
    with open(file_path, 'r') as file:
        return load(file)

def validate_server_filename(server):
    """Validate that the server file name is all lowercase."""
    if not server.islower():
        raise ValueError(f'Invalid server file name (must be all lowercase): {server}')

def validate_server_json(server_json):
    """Validate the server JSON data against the schema."""
    validate(server_json, schema)

def process_server_file(file_path, schema):
    """Process and validate a single server file."""
    server_json = load_json(file_path)
    validate_server_json(server_json)
    server_name = os.path.splitext(os.path.basename(file_path))[0]
    return server_name, server_json

def get_servers(directory, schema):
    """Load and validate all server files in the given directory."""
    servers = {}
    for server in listdir(directory):
        print(f'Validating {server}...', end=' ')
        try:
            validate_server_filename(server)
            server_name, server_json = process_server_file(os.path.join(directory, server), schema)
            servers[server_name] = server_json
            print('OK')
        except Exception as e:
            print('FAILED')
            raise ValueError(f'Invalid server file: {server}') from e
    return servers

def save_index(data, file_path):
    """Save the data to the given file path as JSON."""
    with open(file_path, 'w') as file:
        dump(data, file)

if __name__ == '__main__':
    schema = load_json('server.schema.json')
    servers = get_servers('servers', schema)
    print('Saving index...', end=' ')
    try:
        save_index(servers, 'servers.json')
        print('OK')
    except Exception as e:
        print('FAILED')
        raise e
