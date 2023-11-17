import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title=None, contents=None): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        if title == None or len(title) <= 0 or contents == None or len(contents) <= 0:
            raise Exception("Invalid entry, 'title' and 'contents' must have at least one character.")
        if len(contents) > 0:
            self.title = title
            self.contents = contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        if self.contents:
            words = self.contents.split()
            return len(words)
        else:
            return 0

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        words = self.count_words()
        minutes = math.ceil(words / wpm)
        return minutes

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
        self.contents_tracker = ''
        if len(self.contents_tracker) > 0:
            result = self.contents_tracker.split()
            self.contents_tracker = ''
        else:
            self.contents_tracker = self.contents
            result = self.contents_tracker.split()[:(wpm * minutes)]
            self.contents_tracker = ' '.join(self.contents_tracker.split()[(wpm * minutes):])

        return ' '.join(result)
    

# diary_entry = DiaryEntry('15/11/2023 Gym', 'Completed upper body day 1 weightlifting program today')
# result = diary_entry.count_words()
# print(result)