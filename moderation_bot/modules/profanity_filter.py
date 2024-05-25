profanity_filter.py:
# profanity_filter.py

import profanity_filter

class ProfanityFilter:
    def __init__(self):
        self.filter = profanity_filter.ProfanityFilter()

    def check_profanity(self, message):
        return self.filter.is_profane(message)

    def censor_profanity(self, message):
        return self.filter.censor(message)

    def remove_profanity(self, message):
        return self.filter.remove_bad_words(message)

# End of profanity_filter.py