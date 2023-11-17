import pytest
from lib.diary_entry import *

"""
Given an instance of the class with title / contents
#count_words Sets the title and contents properties (no return)
"""
def test_if_counts_words():
    diary_entry = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    result = diary_entry.count_words()
    assert result == 8


"""
Given an instance of the class with title / contents
#reading_time returns reading time in minutes for the contents at the given wpm
"""
def test_if_calculates_reading_time():
    diary_entry = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    result = diary_entry.reading_time(2)
    assert result == 4


"""
Given an instance of the class with title / contents
#reading_chunk returns a chunk of the contents that the user could read in the given number of minutes
"""
def test_if_can_read_chunk():
    diary_entry = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    result = diary_entry.reading_chunk(2, 3)
    assert result == 'Completed upper body day 1 weightlifting'


"""
When class is instantiated without arguments
#DiaryEntry throws an error
"""
def test_if_throws_error_when_no_arguments():
    with pytest.raises(Exception) as e: 
        DiaryEntry()
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'contents' must have at least one character."


"""
When class is instantiated with one empty string as argument
#DiaryEntry throws an error
"""
def test_if_throws_error_when_empty_arguments():
    with pytest.raises(Exception) as e: 
        DiaryEntry('15/11/2023 Gym', '')
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'contents' must have at least one character."