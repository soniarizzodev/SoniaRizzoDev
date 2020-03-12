import todoist
from webapp.api.get_api import get_api
from webapp.api.Response import Response

def get_tasks(*kwargs):

    api = todoist.api.TodoistAPI(get_api())

    api.sync()

    tasks_names = []

    # Get tech project from todoist
    tech_project = next((project for project in api.state['projects'] if 'tech' in project['name'].lower()), None)   

    if tech_project is not None:
        # Get all tasks belonging to tech project
        tech_proj_id = tech_project['id']

    
        for task in api.state['items']:
            if task['project_id'] == tech_proj_id and not task['checked'] and not task['in_history'] and not task['is_deleted']:
                tasks_names.append(task['content'])

    response = Response(True)

    response.add("tasks", tasks_names)

    return response.compose()