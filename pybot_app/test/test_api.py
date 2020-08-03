import urllib.request
from pybot_app.actions.api_request_wiki import ApiRequester
from .results import results as results_wiki
from pybot_app.actions.parsing import Parser


def test_api(monkeypatch):
    api = ApiRequester()
    results = 48.85837009999999, 2.2944813
    len_results_wiki = len(results_wiki)

    def monkeyreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', monkeyreturn)
    assert api.get_geocode('eiffel') == results
    assert len(api.get_data_wiki('OpenClassrooms')) == len_results_wiki


def test_parsing():
    parser = Parser()
    return_parser = parser.filter_words(
        "Salut pybot donnes moi l'adresse d'OpenClassrooms")
    expected = "OpenClassrooms"
    assert return_parser == expected
