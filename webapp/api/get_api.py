import os 
from webapp.vars import HEROKU_DEPLOY

def get_api():
    if not HEROKU_DEPLOY:    
        from webapp.api.config import api_key
        return api_key
    else:
        return os.getenv('TODOIST_API_KEY')
