from flask import Flask, render_template, request, jsonify, escape
from .actions.parsing import Parser
from .actions.api_requester import ApiRequester
from .actions.list_anectdote import ListAnectdote
from random import randint


app = Flask(__name__)
app.config.from_object('config')

parser = Parser()
api_requester = ApiRequester()
anectode = ListAnectdote()


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    '''
        Get the query from the user input
        parse it to get rid of the stop word
        finally append the usefull words to create a query
    '''
    # Get the query from the user input
    query = escape(request.get_data(as_text=True))
    # Parse the query to retrieve the essentials words

    # filtered_query, ad_wanted, info_wanted = parser.filter_words(str(query))
    filtered_query = parser.layer_filter(query)
    try:
        if len(filtered_query) > 1:
            filtered_query = " ".join(filtered_query)
        # Get the position and address for the query
        lat, lng = api_requester.get_geocode(filtered_query)
        # Trigger the Wiki API to get informations about the location
        list_articles = api_requester.get_list_wiki_geocode(
            lat, lng)
        informations = api_requester.get_article_wiki(list_articles)

    except Exception as e:
        print(f"Exception occured : {e}")
        lat, lng = 0, 0
        informations = "... Pas d'info mais une anectdote : "
        informations += anectode.return_anectdote[randint(
            0, len(anectode.return_anectdote) - 1)]
    # Return the differents informations in a JSON format
    return jsonify(query, informations,
                   lat, lng)
