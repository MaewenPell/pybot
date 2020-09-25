from .list_stop_words import ListStopWords


class Parser():
    def __init__(self):
        self.list = ListStopWords()

    def pattern_exepected(self):
        '''
            Simulation of severals sentences that can be
            entered by the user.

            return list(pattern)
        '''
        p_1 = "Salut pybot donnes moi des informations sur"
        p_2 = "Tu connais l adresse de"
        p_3 = "Ou est"
        p_4 = "Donnes moi l adresse de"
        p_5 = "Est ce que connais ?"
        p_6 = "Salut Pybot donnes moi des informations et l adresse"

        return [elem for elem in (p_1, p_2, p_3, p_4, p_5, p_6)]

    def normalize_query(self, query):
        query = query.replace("-", " ")
        query = query.replace("&#39;", "'")
        query = query.replace("'", " ")
        query = query.lower()
        query = query.split(' ')

        return query

    def layer_filter(self, query):
        '''
            We take the query and substract it with our
            predefined pattern
        '''
        usefull_words = []
        pattern_words = []

        # First we normalize the query
        query = self.normalize_query(query)

        # We remove the stop words
        query = [word for word in query if word not in self.list.return_list()]

        print(f"Query after normalization : {query}")
        # We create a list of all our pattern word that need to be extracted
        for sentences in self.pattern_exepected():
            pattern_words += sentences.split()
        pattern_words = [word.lower() for word in pattern_words]

        # We isolate the first batch of word that left from our first layer
        usefull_words = [
            word for word in query if word not in pattern_words and len(word) > 1]
        return usefull_words

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
