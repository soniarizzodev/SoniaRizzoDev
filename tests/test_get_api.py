import pytest
from webapp.api.get_api import get_api

def test_get_api():
    td_api_key = get_api()
    
    assert td_api_key != ''
    assert td_api_key != None    
  