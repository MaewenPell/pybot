from pybot_app.actions.parsing import Parser
from pybot_app.actions.list_stop_words import ListStopWords


class TestParsing:
    PARSER = Parser()
    LIST = ListStopWords()

    # Batch of test to try differents input

    def test_parsing(self):
        return_parser, _, _ = self.PARSER.filter_words(
            "Salut pybot donnes moi l'adresse d'OpenClassrooms")
        expected = "OpenClassrooms"
        assert return_parser == expected

    def test_parsing_2(self):
        return_parser, _, _ = self.PARSER.filter_words(
            "Donnes moi des informations sur Marseille please"
        )
        expected = "Marseille"
        assert return_parser == expected

    def test_parsing_3(self):
        return_parser, _, _ = self.PARSER.filter_words(
            "Paris")
        expected = "Paris"
        assert return_parser == expected

    # Test for empty query
    def test_empty(self):
        return_parser = self.PARSER.filter_words("")
        print(return_parser)
        assert return_parser == "empty"

    def test_remove(self):
        return_parser, _, _ = self.PARSER.filter_words("-")
        assert return_parser == ""

    def test_remove_2(self):
        return_parser, _, _ = self.PARSER.filter_words("'")
        assert return_parser == ""

    def test_not_usefull_word(self):
        assert "a" in self.LIST.return_list() \
            and "ô" in self.LIST.return_list()
