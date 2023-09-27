import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')


unvalid_email = os.getenv('unvalid_email')
unvalid_password =os.getenv('unvalid_password')