import todoist
import json
from webapp.api.get_api import get_api
from webapp.api.srd_todoist import get_tasks
from webapp import app

def test_todoist():
    api = todoist.api.TodoistAPI(get_api())
    
    assert api != None
    assert api != {}
    
    api.sync()

    assert api != {}
    assert api.state['user']['full_name'] == 'Sonia Rizzo'
   
def test_get_tasks():
    with app.app_context():
    
        response = get_tasks()

        assert response != None
        assert response != ''
        assert response.status_code == 200

        assert response.data != b'{}'

        response_content = response.json

        assert 'data' in response_content
        assert 'tasks' in response_content['data']
