from pybot_app.actions.api_requester import ApiRequester
from pybot_app.actions.parsing import Parser
from pybot_app.actions.list_stop_words import ListStopWords


class TestApi:
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


class TestParsing:
    PARSER = Parser()
    LIST = ListStopWords()

    def test_parsing(self):
        return_parser = self.PARSER.filter_words(
            "Salut pybot donnes moi l'adresse d'OpenClassrooms")
        expected = "OpenClassrooms"
        assert return_parser == expected

    def test_parsing_2(self):
        return_parser = self.PARSER.filter_words(
            "Donnes moi des informations sur Marseille please"
        )
        expected = "Marseille"
        assert return_parser == expected

    def test_parsing_3(self):
        return_parser = self.PARSER.filter_words(
            "Paris")
        expected = "Paris"
        assert return_parser == expected

    def test_not_usefull_word(self):
        assert "a" in self.LIST.return_list() \
            and "ô" in self.LIST.return_list()

