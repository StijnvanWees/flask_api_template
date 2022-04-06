import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()


credentials = (os.getenv("DEFAULT_USER"), os.getenv("DEFAULT_PASSWORD"))
if len(sys.argv) == 3:
    credentials = (sys.argv[1], sys.argv[2])


response = requests.post(f"http://{os.getenv('APP_HOST')}:{os.getenv('APP_PORT')}/get_token",
                         auth=(os.getenv("DEFAULT_USER"), os.getenv("DEFAULT_PASSWORD")))
print(response.json())
