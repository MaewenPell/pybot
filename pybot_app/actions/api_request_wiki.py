import requests
class ApiRequester():
    '''
        Fetch data from wikicommons website
    '''
    def __init__(self):
        pass

    def get_data(self, query):
        req = f"https://fr.wikipedia.org/api/rest_v1/page/related/{query}"
        r = requests.get(req)
        r = r.json()
        information = r['pages'][0]['extract']
        return information
