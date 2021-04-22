import os
from dotenv import load_dotenv

class Config(object):

    load_dotenv()
    # Obtener un token de bot de botfather
    Token = os.getenv('Token')
    # Obtener en https://my.telegram.org/apps
    api_id = os.getenv('api_id')
    # Obtener en https://my.telegram.org/apps
    api_hash = os.getenv('api_hash')