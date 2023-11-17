import re

class PhoneNumbers:
    def __init__(self, list_of_entries):
        self.list_of_entries = list_of_entries

    # search all diary entries for phone numbers and make a list of phone numbers
    def list_of_mobile_phone_numbers(self):
        phone_numbers = []
        uk_phone_regex = r'\b0[0-9]{10}\b'
        for obj in self.list_of_entries:
            phone_numbers += re.findall(uk_phone_regex, obj.contents)
        if len(phone_numbers) > 0:
            return phone_numbers
        else:
            raise Exception("No valid phone numbers found.")