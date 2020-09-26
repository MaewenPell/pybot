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

    def get_list_wiki_geocode(self, lat, lng):
        '''
            We trigger the wiki API to get a list
            of article related to the lat, lng provided

            :params:
            lat -> (int) latitude of the request
            lng -> (int) longitude of the request
        '''
        params_wiki = {
            "format": "json",
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": f"{lat}|{lng}"
        }
        r = requests.get(self.base_url_wiki, params=params_wiki)
        if r.status_code != 200:
            print(f'Error accessing API ressource: {r.status_code}')
        else:
            r = r.json()
            list_article = r['query']['geosearch']

        return list_article

    def get_article_wiki(self, article_list):
        '''
            We triggerd the API of wikipedia to retrieve
            the first article (the closest in regards of the geocode)

            :params:
            article -> dict
        '''
        # We parse the article list to find the pageid
        page_id = article_list[0]['pageid']
        params = {
            "format": "json",
            "action": "query",
            "prop": "extracts|info",
            "inprop": "url",
            "exchars": 1200,
            "explaintext": 1,
            "pageids": page_id
        }

        # we trigger the request:
        r = requests.get(self.base_url_wiki, params=params)
        if r.status_code != 200:
            print(f'Error accessing API ressource: {r.status_code}')
        else:
            r = r.json()
            article = r['query']['pages'][str(page_id)]['extract']

        return article

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
            lat = location['lat']
            lng = location['lng']

        return lat, lng
