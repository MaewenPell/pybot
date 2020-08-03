import requests
from config import MAPS_API_KEY

class ApiRequester():
    '''
        Create the differents request for the external API
    '''

    def __init__(self):
        self.base_url_wiki = "https://fr.wikipedia.org/w/api.php"
        self.base_url_map = "https://maps.googleapis.com/maps/api/geocode/json"

    def get_data_wiki(self, query):
        """[summary]
            Trigger the Wikicommon API with the query
            to retrieve the results:
        Args:
            query ([str]): [Filtered query]

        Returns:
            information [str]: [Wiki paragraph]
        """
        r = requests.get(self.base_url_wiki,
                         params={'format': 'json',
                                 'action': 'query',
                                 'prop': 'extracts',
                                 'exintro': 1,
                                 'explaintext': 1,
                                 'redirects': 1,
                                 'titles': query,
                                 })
        if r.status_code != 200:
            information = f'Error accessing API ressource : {r.status_code}'
        else:
            r = r.json()
            for elem in (r['query']['pages']):
                if elem == '-1':
                    information = 'No data found with this request'
                else:
                    information = r['query']['pages'][elem]['extract']

        return information

    def get_geocode(self, address):
        """[summary]

        Args:
            address (str): Filtered Query

        Returns:
            int, int: lat, lng used to place the marker on the map
        """
        r = requests.get(self.base_url_map,
                         params={
                             'address': address,
                             'key': MAPS_API_KEY
                         })
        if r.status_code != 200:
            lat, lng = 0, 0
            print(f'Error accessing API ressource: {r.status_code}')
        else:
            r = r.json()
            location = r["results"][0]["geometry"]["location"]
            lat = location['lat']
            lng = location['lng']

        return lat, lng
