"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

"""
import sys
import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne'
}


def capital_of_Idaho():
    '''Print the state capital of Idaho'''
    if len(STATES_CAPITALS) == 0:
        raise KeyError
    print(STATES_CAPITALS['Idaho'])
    pass

def all_states():
    '''Print all states'''
    if len(STATES_CAPITALS) == 0:
        raise KeyError
    for state in STATES_CAPITALS:
        print(state)
    pass

def all_capitals():
    '''Print all capitals'''
    if len(STATES_CAPITALS) == 0:
        raise KeyError
    for capital in STATES_CAPITALS.values():
        print(capital)
    pass

def states_capitals_string():
    '''Print a single string of the list 'Alabama -> Montgomery, Alaska -> Juneau, ...' '''
    if len(STATES_CAPITALS) == 0:
        raise KeyError
    all_strings = ""
    sorted_dict = dict(sorted(STATES_CAPITALS.items()))
    for state, capital in sorted_dict.items():
        all_strings +=state + " -> " + capital + ", "
        #all_strings.sort() 
    print(all_strings[0:-2])
    return(all_strings[0:-2])



def get_state(capital):
    '''Given a capital, return the state, if there are multiple states with the same capital, return a list of states'''
    #matched_state = list(sorted_dict.keys())[list(sorted_dict.values()).index(capital)]
    #print(matched_state)
    if len(STATES_CAPITALS) == 0:
        return KeyError
    sorted_dict = dict(sorted(STATES_CAPITALS.items()))
    matched_state = []
    for country, city in sorted_dict.items():
        if capital == city:
            matched_state.append(country)
    if  len(matched_state) == 1:
        print (matched_state[0])
        return(matched_state[0])
    elif len(matched_state) > 1:
        print(matched_state)
        return(matched_state)
    else:
        print("No match found")
        raise KeyError
        


def get_capital(state):
    '''Given a state, return the capital, if there are multiple capitals with the same state, return a list of captials'''
    #matched_capitol = list(sorted_dict.values())[list(sorted_dict.keys()).index(state)]
    #print(matched_capitol)
    if len(STATES_CAPITALS) == 0:
        return KeyError
    sorted_dict = dict(sorted(STATES_CAPITALS.items()))
    matched_capital = []
    for country, city in sorted_dict.items():
        if state == country:
            matched_capital.append(city)
    if  len(matched_capital) == 1:
        print (matched_capital[0])
    elif len(matched_capital) > 1:
        print(matched_capital)
    else:
        print("No match found")
        raise KeyError


def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    
    '''Manual Outputs for testing and proof of work'''
    print('--------------------------------------')
    print('task 1 - captial of Idaho')
    print('--------------------------------------')
    capital_of_Idaho()
    print('--------------------------------------')
    print('task 2 - all states')
    print('--------------------------------------')
    all_states()
    print('--------------------------------------')
    print('task 3 - all capitals')
    print('--------------------------------------')
    all_capitals()
    print('--------------------------------------')
    print('task 4 - all states and capitals')
    print('--------------------------------------')
    states_capitals_string()
    print('--------------------------------------')
    print('task 5 - get state from capital')
    print('--------------------------------------')
    get_state('Cheyenne')
    print('--------------------------------------')
    print('task 6 - get capital from state')
    print('--------------------------------------')
    get_capital('Wyoming')
    retcode = pytest.main([__file__])
    sys.exit(main())
