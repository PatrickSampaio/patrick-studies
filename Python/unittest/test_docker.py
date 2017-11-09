from mock import patch
import os

@patch("unittest.docker_app.get_random_person")
def test_new_person(mock_get_random_person):
    from unittest.docker_app import get_next_person
    #arranger
    user = {'people_seen':[]}
    expected_person = 'Katie'
    mock_get_random_person.return_value = 'Katie'

    actual_person = get_next_person(user)
    assert actual_person == expected_person
