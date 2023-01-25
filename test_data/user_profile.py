from utils.random_generator import random_word


class UserProfile:
    def __init__(self):
        self._firstname = random_word()
        self._email = "test@test.com"
        self._lastname = random_word()

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def email(self):
        return self._email


new_user = UserProfile()
