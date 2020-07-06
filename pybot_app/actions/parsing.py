from .list_stop_words import list_
import googlemaps


class Parser():
    def __init__(self, key):
        self.stop_words = list_
        self.key = key
        self.gmaps = googlemaps.Client(key=key)

    def filter_words(self, query):
        ''' Parse the query to get the usefull words
        @input : user_query(list) or str
        @return : list of words not in stop_word list
        '''
        usefull_words = []
        for word in self.stop_words:
            if word not in self.stop_words:
                usefull_words.append(word)
        return usefull_words

    def get_geocode(self, place):
        ''' Request '''
        try:
            geocode_result = self.gmaps.geocode(place)
        except ValueError:
            print(
                'Error Either credentials are missing, incomplete or invalid.')
            return False
        return geocode_result
