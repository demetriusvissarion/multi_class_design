import math
# from diary_entry import *

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
        self.list_of_entries.append(entry)

    def all(self):
        if len(self.list_of_entries) <= 0:
            raise Exception("No entry.")
        # Returns:
        #   A list of instances of DiaryEntry

        if len(self.list_of_entries) > 1:
            result = ''
            for entry in self.list_of_entries:
                result += entry.title + ': ' + entry.contents + ', \n'
            return result
        elif len(self.list_of_entries) == 1:
            return self.list_of_entries[0].title + ': ' + self.list_of_entries[0].contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        result = 0
        for object in self.list_of_entries:
            result += object.count_words()
        return result

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        result = 0
        for object in self.list_of_entries:
            result += object.reading_time(wpm)
        return result

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

        # can_read = wpm * minutes
        dict_of_each_entry_reading_time = {}
        for object in self.list_of_entries:
            dict_of_each_entry_reading_time[object.title] = object.reading_time(wpm)
        # iterate through that list and find the number that is closest to, but not over (see below code)
        smaller_dict = {}
        for key, value in dict_of_each_entry_reading_time.items():
            if value <= minutes:
                smaller_dict[key] = value
        values = smaller_dict.values()
        biggest_value = max(values)
        result = ''
        for key, value in smaller_dict.items():
            if value == biggest_value:
                result += key
        return result


# # find the number that is closest to, but not over
# my_list = [1, 3, 5, 7, 9, 11]
# def find_closest_but_not_over(input_number):
#     smaller_list = []
#     for number in my_list:
#         if number <= input_number:
#             smaller_list.append(number)
#     result = max(smaller_list)
#     return result
# print(find_closest_but_not_over(2))


# entry = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
# diary = Diary()
# diary.add(entry)
# result = diary.all()