from flask import Flask, render_template, request, jsonify, escape
from .actions.parsing import Parser
from .actions.api_requester import ApiRequester


app = Flask(__name__)
app.config.from_object('config')

parser = Parser()
api_requester = ApiRequester()


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
    filtered_query, ad_wanted, info_wanted = parser.filter_words(str(query))
    try:
        if filtered_query != "empty":
            # print(f"Filtered query = {filtered_query}")
            # Get the position and address for the query
            lat, lng, _, address = api_requester.get_geocode(filtered_query)
            # Trigger the Wiki API to get informations about the location
            if info_wanted:
                informations = api_requester.get_data_wiki(filtered_query)
            else:
                informations = "Je n'ai pas trouvé d'informations :("
        else:
            lat, lng = 0, 0
            informations = "La reqûete me semble vide ?"
    except IndexError:
        lat, lng = 0, 0
        address = "Je n'ai pas trouvé d'addresse pour cette requête"
        informations = "Je n'ai pas trouvé d'informations pour cette requête"
    # Return the differents informations in a JSON format
    return jsonify(query, informations,
                   lat, lng, address,
                   ad_wanted, info_wanted)
