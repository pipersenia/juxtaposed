import os
from dotenv import load_dotenv
load_dotenv()

subscription_key = os.getenv('SUBSCRIPTION_KEY')
endpoint = os.getenv('ENDPOINT')
