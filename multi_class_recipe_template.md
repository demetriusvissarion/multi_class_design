# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._


"As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries => search all entries for phone numbers and make a list of phone numbers"


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
....
```

_Also design the interface of each class in more detail._

```python
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string
    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.

class Diary:
    def __init__(self):
        self.list_of_entries = []
        self.words_count = {}

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task = ''):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True

class TodoList:
    def __init__(self):
        self.todos_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        
    def complete_and_incomplete_helper(self, my_list, boolean):
        # added this method for DRY

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

import pytest
from lib.diary import *
from lib.diary_entry import *


"""
Given an instance of DiaryEntry and one entry
#add Adds the entry to the entries list
"""
def test_if_entry_added():
    entry = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    # entry = [diary_entry.title, diary_entry.contents]
    # print(entry)
    diary = Diary()
    diary.add(entry)
    result = diary.all()
    assert result == '15/11/2023 Gym: Completed upper body day 1 weightlifting program today'



"""
Given an instance of DiaryEntry and two entries
#add Adds the entries to the entries list
"""
def test_if_two_entries_added():
    diary_entry1 = DiaryEntry('14/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.all()
    assert result == '14/11/2023 Gym: Completed upper body day 1 weightlifting program today, \n15/11/2023 Latin Lesson: Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci., \n'



"""
When all() function is called after adding entries
#all returns a list of all entries
"""
def test_if_shows_all_entries():
    diary_entry1 = DiaryEntry('13/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('14/11/2023 Gym', 'Completed upper body day 2 weightlifting program today')
    diary_entry3 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.all()
    assert result == '13/11/2023 Gym: Completed upper body day 1 weightlifting program today, \n14/11/2023 Gym: Completed upper body day 2 weightlifting program today, \n15/11/2023 Latin Lesson: Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci., \n'


"""
When count_words() function is called after adding entries
#count_words returns an integer representing the number of words in all diary entries
"""
def test_if_counts_words_in_all_entries():
    diary_entry1 = DiaryEntry('13/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('14/11/2023 Gym', 'Completed upper body day 2 weightlifting program today')
    diary_entry3 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    result = diary.count_words()
    assert result == 75


"""
When reading_time() function is called after adding entries
#reading_time returns an integer of reading time in minutes if user reads all entries
"""
def test_if_calculates_reading_time():
    diary_entry1 = DiaryEntry('14/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 2 weightlifting program today')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.reading_time(2)
    assert result == 8


"""
When find_best_entry_for_reading_time() function is called after adding entries
#find_best_entry_for_reading_time returns best entry to read
"""
def test_if_finds_best_entry_for_reading_time():
    diary_entry1 = DiaryEntry('14/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(2, 5)
    assert result == '14/11/2023 Gym'



"""
When all() function is called without adding entries
#all throws an error
"""
def test_throws_error_when_no_entries():
    diary = Diary()
    with pytest.raises(Exception) as e: 
        diary.all()
    error_message = str(e.value)
    assert error_message == "No entry."
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

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
def test_if_throws_error_when_no_arguments():
    with pytest.raises(Exception) as e: 
        DiaryEntry('15/11/2023 Gym', '')
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'contents' must have at least one character."
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


