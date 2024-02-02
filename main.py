import os
from dotenv import load_dotenv

load_dotenv()

email : str = os.getenv('EMAIL')
senha : str = os.getenv('SENHA')

print(email, senha)