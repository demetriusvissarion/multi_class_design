import pytest
from lib.diary import *
from lib.diary_entry import *
from lib.phone_numbers import *


"""
When list_of_mobile_phone_numbers() function is called after adding entries
#list_of_mobile_phone_numbers returns phone numbers of 10 numbers only
"""
def test_if_list_of_mobile_phone_numbers_returns_phone_numbers():
    diary_entry1 = DiaryEntry('14/11/2023 Gym', '074758447611 Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci 07475844761 luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. 07475844766 Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    get_phone_numbers = PhoneNumbers(diary.list_of_entries)
    result = get_phone_numbers.list_of_mobile_phone_numbers()
    assert result == ['07475844761', '07475844766']


"""
When list_of_mobile_phone_numbers() function is called after adding entries
#list_of_mobile_phone_numbers thows error if no valid phone numbers
"""
def test_throws_error_when_no_valid_phone_numbers():
    diary_entry1 = DiaryEntry('14/11/2023 Gym', '074758447611 Completed upper body day 1 weightlifting program today')
    diary_entry2 = DiaryEntry('15/11/2023 Latin Lesson', 'Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci 0747584761 luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. 97475844766 Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci.')
    diary = Diary()
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    get_phone_numbers = PhoneNumbers(diary.list_of_entries)
    with pytest.raises(Exception) as e: 
        get_phone_numbers.list_of_mobile_phone_numbers()
    error_message = str(e.value)
    assert error_message == "No valid phone numbers found."