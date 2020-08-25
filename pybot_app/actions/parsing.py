from .list_stop_words import ListStopWords


class Parser():
    def __init__(self):
        self.list = ListStopWords()

    def filter_words(self, query):
        ''' Parse the query to get the usefull words
            input : user_query(list) or str
            @return : list of words not in stop_word list
        '''
        address_wanted = False
        info_wanted = False
        if query != "":
            usefull_words = []
            query = query.replace("-", " ")
            query = query.replace("&#39;", "'")
            query = query.replace("'", " ")
            query = query.split(' ')
            query[0].lower()
            for elem in query:
                if elem == "addresse" or elem == "adresse":
                    address_wanted = True
                elif (elem == "info" or elem == 'information'
                      or elem == 'informations'):
                    info_wanted = True
            for word in query[-4:]:
                if word not in self.list.return_list():
                    usefull_words.append(word)
            return usefull_words[0], address_wanted, info_wanted
        else:
            return "empty"
