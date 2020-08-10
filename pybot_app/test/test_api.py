from pybot_app.actions.api_requester import ApiRequester


class TestMockApi:
    API = ApiRequester()

    def test_mock_wiki(self, monkeypatch):
        results = "Good results for OpenClassrooms request"

        def mockreturn(request):
            return results

        monkeypatch.setattr(self.API, 'get_data_wiki', mockreturn)

        assert self.API.get_data_wiki('OpenClassRooms' == results)

    def test_mock_geocode(self, monkeypatch):
        results = 48.85837009999999, 2.2944813

        def mockreturn(request):
            # print(results)
            return results

        monkeypatch.setattr(self.API, 'get_geocode', mockreturn)

        assert self.API.get_geocode('eiffel') == results


class TestApi:
    API = ApiRequester()

    def test_return_wiki(self):
        fetched_data = self.API.get_data_wiki("Nantes")
        test_data = fetched_data[:163]
        expected = (
            "Nantes (/nɑ̃t/ ) " +
            "est une commune de l'ouest de la France, située " +
            "au sud du Massif armoricain, qui s'étend sur les " +
            "rives de la Loire, à 50 km de l'océan Atlantique.")
        assert test_data == expected

    def test_return_geo(self):
        fetch_geo = self.API.get_geocode("Nantes")
        exp_lat, exp_lng = 47.218371, -1.553621
        assert fetch_geo[0] == exp_lat
        assert fetch_geo[1] == exp_lng

    def test_status_code_geo(self):
        _, _, r = self.API.get_geocode("Nantes")
        assert r['status'] == "OK"

    # def test_status_code_wiki(self):
    #     _, r = self.API.get_data_wiki("Nantes")
