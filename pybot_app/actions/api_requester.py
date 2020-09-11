import requests
from config import MAPS_API_KEY


class ApiRequester():
    '''
        Create the differents request for the external API
    '''

    def __init__(self):
        self.base_url_wiki = "https://fr.wikipedia.org/w/api.php"
        self.base_url_map = "https://maps.googleapis.com/maps/api/geocode/json"
        self.params_wiki = {'format': 'json',
                            'action': 'query',
                            'prop': 'extracts',
                            'exintro': 1,
                            'explaintext': 1,
                            'redirects': 1,
                            'titles': 'query',
                            }

    def get_data_wiki(self, query):
        """[summary]
            Trigger the Wikicommon API with the query
            to retrieve the results:
        Args:
            query ([str]): [Filtered query]

        Returns:
            information [str]: [Wiki paragraph]
        """
        self.params_wiki["titles"] = query
        r = requests.get(self.base_url_wiki,
                         params=self.params_wiki)
        if r.status_code != 200:
            information = f'Error accessing API ressource : {r.status_code}'
        else:
            r = r.json()
            for elem in (r['query']['pages']):
                if elem == '-1':
                    information = ("Pas d'info ... verifiez l'écriture ? :) ")
                else:
                    information = r['query']['pages'][elem]['extract']

        if information == "":
            information = "Pas d'info sur wikipédia pour cette reqûete :("
        return information

    def get_geocode(self, address):
        """[summary]

        Args:
            address (str): Filtered Query

        Returns:
            lat(int), lng(int) used to place the marker on the map
            address of the query
            r (int) = response status
            formated_adress (str) : the addresse of the query
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
            formated_address = r["results"][0]["formatted_address"]
            lat = location['lat']
            lng = location['lng']

        return lat, lng, r, formated_address
