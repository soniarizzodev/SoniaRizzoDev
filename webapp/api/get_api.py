import os
from webapp.api import config
from webapp.vars import HEROKU_DEPLOY

def get_api():
    if not HEROKU_DEPLOY:    
        return config.api_key
    else:
        return os.getenv('TODOIST_API_KEY')
