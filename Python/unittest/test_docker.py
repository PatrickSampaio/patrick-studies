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

@patch.object(Application, "get_random_person")
def test_new_person_side_effect(mock_get_random_person):
    #arranger
    app = Application()
    user = {'people_seen':['Sarah', 'Mary']}
    expected_person = 'Katie'

    mock_get_random_person.side_effect = ['Mary', 'Sarah', 'Katie']
   
    actual_person = app.get_next_person(user)
    assert actual_person == expected_person

####Behavior Test

@patch.object(Application, "send_email")
@patch.object(Application, "let_down_gently")
@patch.object(Application, "give_it_a_time")
def test_matching_behavior(mock_give_it_a_time,
                           mock_let_down_gently,
			   mock_send_email):
    app = Application()
    person1 = { 'name': 'Bil', 'likes':['Sarah'], 'dislikes': [] }
    person2 = { 'name': 'Sarah', 'likes': [], 'dislikes' : ['Bil']}

    app.evaluate(person1, person2)
    
    
    mock_let_down_gently.assert_called_once_with(person1['name'])
    assert mock_give_it_a_time.call_count == 0
    assert mock_let_down_gently.call_count == 1

@patch.object(Application, "send_email")
@patch.object(Application, "let_down_gently")
@patch.object(Application, "give_it_a_time")
def test_matching_behavior_match(mock_give_it_a_time,
                           mock_let_down_gently,
                           mock_send_email):
    app = Application()
    person1 = { 'name': 'Bil', 'likes':['Sarah'] }
    person2 = { 'name': 'Sarah',  'likes' : ['Bil'], 'dislikes': ['Sam']}    
    app.evaluate(person1, person2)


    first_call = mock_send_email.call_args_list[0]
    second_call = mock_send_email.call_args_list[1]

    assert first_call[0][0] == person1['name']
    assert second_call[0][0] == person2['name']













