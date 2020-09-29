"""
user class module
"""

class User:
    user_profile={}  # to keep user profile

    # constructor
    def __init__(self, first, last, middle=""):
        self.first = first
        self.last = last
        self.middle = middle

    def build_profile(self, **user_info) :
        # will put everything we know about user in user_info dict
        self.user_profile['first'] = self.first
        self.user_profile['last'] = self.last
        if self.middle :
            self.user_profile['middle'] = self.middle
        for key, value in user_info.items():
            self.user_profile[key] = value

    def print_profile(self):
        print(f'User profile: ')
        for key, value in self.user_profile.items():
            print(f'\t{key} = {value}')
