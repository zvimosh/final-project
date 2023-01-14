"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest

a_string = 'monty pythons flying circus'
def no_duplicates(a_string):
    '''Returns a sorted string with no duplicate characters'''
    none_duplicates = ''.join(sorted(set(a_string.lower())))
    return none_duplicates


def reversed_words(a_string):
    '''Returns the words in reverse order'''
    a_list = a_string.split()
    reversed_list = a_list[::-1]
    return reversed_list
    


def four_char_strings(a_string):
    '''Returns a list of 4 character strings'''
    four_char = ([a_string[i:i+4] for i in range(0, len(a_string), 4)])
    return four_char



def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    '''Manual Outputs for testing and proof of work'''
"""     print('--------------------------------------')
    print('task 1 - none duplicates, sorted')
    print('--------------------------------------')
    print(no_duplicates(a_string))
    print('--------------------------------------')
    print('task 2 - reversed words')
    print('--------------------------------------')
    print(reversed_words(a_string))
    print('--------------------------------------')
    print('task 3 - 4 char strings')
    print('--------------------------------------')
    print(four_char_strings(a_string))
    print('--------------------------------------')
    retcode = pytest.main([__file__]) """
    
    
    