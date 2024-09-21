import json
file_path=r"api.json"

def load_config(file_path):
    """Load the configuration from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return {}

def get_api_key():
    """Fetch the API key from the configuration file."""
    config = load_config('api.json')
    return config.get('api_key', 'Key not found')

# Main function
def main():
    my_api_key = get_api_key()
    return my_api_key







#import google.generativeai as genai
#def configure(api_key):
 #   genai.configure(api_key='AIzaSyCv-aW0wS9pCujlXiKe1Ttxlpz0jn0TbpQ')
#model = genai.GenerativeModel('gemini-pro')
#print(model)

