file_path=
{
    "api_key":"AIzaSyCv-aW0wS9pCujlXiKe1Ttxlpz0jn0TbpQ"
}
def load_config(file_path):
     """Load the configuration from a JSON file."""
     with open(file_path, 'r') as f:
        #print(f.read())
        return json.load(f)
api_key=load_config(file_path)
print(api_key)







