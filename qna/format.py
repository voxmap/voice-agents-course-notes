import yaml
import json
from datetime import datetime # Import datetime

yaml_file_path = 'qna/format.yaml'
json_file_path = 'qna/format.json' # This will overwrite the previous JSON file

# Custom serializer for datetime objects
def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

try:
    with open(yaml_file_path, 'r', encoding='utf-8') as yf:
        # Using safe_load is recommended for loading YAML from untrusted sources
        # or just as a general good practice.
        # PyYAML will convert valid ISO 8601 strings to datetime objects
        data = yaml.safe_load(yf)

    with open(json_file_path, 'w', encoding='utf-8') as jf:
        # Use the custom converter for datetime objects
        json.dump(data, jf, indent=2, ensure_ascii=False, default=datetime_converter)

    print(f"Successfully converted '{yaml_file_path}' to '{json_file_path}'")

except FileNotFoundError:
    print(f"Error: The file '{yaml_file_path}' was not found.")
except yaml.YAMLError as e:
    print(f"Error parsing YAML file '{yaml_file_path}': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
