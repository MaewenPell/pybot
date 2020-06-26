from .list_stop_words import list_


class Parser():
    def __init__(self):
        self.stop_words = list_

    def is_stop_words(self, word_to_check):
        for word in self.stop_words:
            if word_to_check in self.stop_words:
                return True
        return False
