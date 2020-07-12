from .list_stop_words import list_


class Parser():
    def __init__(self, key):
        self.stop_words = list_

    def filter_words(self, query):
        ''' Parse the query to get the usefull words
        input : user_query(list) or str
        @return : list of words not in stop_word list
        '''
        usefull_words = []
        for word in query:
            print(word)
            if word not in self.stop_words:
                usefull_words.append(word)
        print(usefull_words)
        return usefull_words

