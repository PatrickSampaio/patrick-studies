from mock import patch
import os

from unittest.docker_app import Application

#@patch("unittest.docker_app.get_random_person")
@patch.object(Application, "get_random_person")
def test_new_person(mock_get_random_person):
    #arranger
    app = Application()
    user = {'people_seen':[]}
    expected_person = 'Katie'

    mock_get_random_person.return_value = 'Katie'

    actual_person = app.get_next_person(user)
    assert actual_person == expected_person
