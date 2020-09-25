from pybot_app.actions.api_requester import ApiRequester


class TestMockApi:
    API = ApiRequester()

    def test_mock_wiki_list(self, monkeypatch):
        class MockResponse():
            def __init__(self, url, params=None):
                self.status_code = 200

            def json(self):
                return {'batchcomplete': '',
                        'query': {'geosearch': [{'dist': 0,
                                                 'lat': 48.856614,
                                                 'lon': 2.3522219,
                                                 'ns': 0,
                                                 'pageid': 7785129,
                                                 'primary': '',
                                                 'title': "Mock Title"},
                                                ]}}

        monkeypatch.setattr('requests.get', MockResponse)
        assert type(self.API.get_list_wiki_geocode(123, 456)) == list

    def test_mock_geocoding(self, monkeypatch):
        class MockResponseMaps():
            def __init__(self, url, params=None):
                self.status_code = 200

            def json(self):
                return {'results': [{'formatted_address': 'Paris, France',
                                     'geometry': {'location': {'lat': 1.1,
                                                               'lng': 2.2}}}]}

        monkeypatch.setattr('requests.get', MockResponseMaps)
        assert self.API.get_geocode('Test') == (1.1, 2.2)

