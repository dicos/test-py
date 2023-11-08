import os
from dotenv import load_dotenv

load_dotenv('.env')


SECRET_KEY = os.environ["AUTH_SECRET"]
ALGORITHM = os.environ["AUTH_ALGO"]
ACCESS_TOKEN_EXPIRE = int(os.environ["AUTH_TOKEN_EXPIRE"])
