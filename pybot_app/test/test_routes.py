import requests


class TestReturnRoutes():
    BASE_URL = "http://127.0.0.1:5000/"

    def testIndex(self):
        r = requests.get(self.BASE_URL)
        assert r.status_code == 200

    def testProcess(self):
        data = "Salut pybot donnes moi des informations sur OpenClassrooms"
        r = requests.post(self.BASE_URL + "/process",
                          data)

        assert r.status_code == 200
