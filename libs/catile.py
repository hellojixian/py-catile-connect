import os
import requests
from dotenv import load_dotenv
load_dotenv()

def difficulty(text:str, title:str|None=None) -> dict:
  endpoint = 'https://enterpriseapi.cathoven.com/catile/difficulty'
  # Set the form data
  data = {
      "client_id": os.environ.get("CATILE_CLIENT_ID"),
      "client_secret": os.environ.get("CATILE_CLIENT_SECRET"),
      "text": text,
      "title": title
  }

  # Send the POST request
  response = requests.post(endpoint, data=data)

  # Check the response status code
  if response.status_code == 200:
      return response.json()
  else:
      print("Request failed with status code:", response.status_code)

def verify_environment():
    if os.environ.get("CATILE_CLIENT_ID") is None:
        raise Exception("CATILE_CLIENT_ID not found in environment variables")
    if os.environ.get("CATILE_CLIENT_SECRET") is None:
        raise Exception("CATILE_CLIENT_SECRET not found in environment variables")

verify_environment()