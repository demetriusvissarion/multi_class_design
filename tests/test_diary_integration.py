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


"""
When list_of_mobile_phone_numbers() function is called after adding entries
#list_of_mobile_phone_numbers returns phone numbers
"""
def test_if_list_of_mobile_phone_numbers_returns_phone_numbers():
    diary_entry1 = DiaryEntry('14/11/2023 Gym', '07475844761 Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. 07475844766 Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.list_of_mobile_phone_numbers()
    assert result == ['07475844761', '07475844766']