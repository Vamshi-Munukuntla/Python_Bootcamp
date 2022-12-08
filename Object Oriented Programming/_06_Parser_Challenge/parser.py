import re


# TODO 1 - Create Parser Class which has text attribute

class Parser:
    def __init__(self, text):
        self.text = text

    # TODO 2 - Create email parser method using regex to find emails
    def email(self):
        match = re.search(r'[a-zA-Z0-9.\-+]+@[a-z0-9.\-+]+\.[a-zA-Z]+', self.text)
        if match:
            return match.group(0)
        return None

    # TODO 3 - Create phone number parser method using regex to find US style phone numbers (xxx-xxx-xxxx)
    def phone(self):
        # match = re.search(r'[0-9]+\-[0-9]+\-[0-9]+', self.text)
        match = re.search(r'\d{3}-\d{3}-\d{4}', self.text)
        if match:
            return match.group(0)
        return None

    def parser(self):
        return {
            'email': self.email(),
            'phone': self.phone()
        }
