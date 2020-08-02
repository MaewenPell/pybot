from .list_stop_words import list_


class Parser():
    def __init__(self):
        self.stop_words = list_

    def filter_words(self, query):
        ''' Parse the query to get the usefull words
            input : user_query(list) or str
            @return : list of words not in stop_word list
        '''
        usefull_words = []
        query = query.replace("-", " ")
        query = query.replace("'", " ")
        query = query.split(' ')
        query[0].lower()
        for word in query[-4:]:
            if word not in list_:
                usefull_words.append(word)
        return usefull_words[0]
