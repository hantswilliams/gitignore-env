import os
from dotenv import load_dotenv

load_dotenv() 

username = 'hants'
password = '123'

username = os.getenv('username')
password = os.getenv('password')