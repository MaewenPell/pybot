from .list_stop_words import ListStopWords


class Parser():
    def __init__(self):
        self.list = ListStopWords()

    def filter_words(self, query):
        ''' Parse the query to get the usefull words
            input : user_query(list) or str
            @return : list of words not in stop_word list
        '''
        if query != "":
            usefull_words = []
            query = query.replace("-", " ")
            query = query.replace("'", " ")
            query = query.split(' ')
            query[0].lower()
            for word in query[-4:]:
                if word not in self.list.return_list():
                    usefull_words.append(word)
            return usefull_words[0]
        else:
            return "empty"
