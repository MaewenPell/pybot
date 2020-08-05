from flask import Flask, render_template, request, jsonify
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
    query = request.get_data(as_text=True)
    # Parse the query to retrieve the essentials words
    filtered_query = parser.filter_words(str(query))
    print(f"Filtered query = {filtered_query}")
    # Get the position for the query
    lat, lng = api_requester.get_geocode(filtered_query)
    # Trigger the Wiki API to get informations about the location
    informations = api_requester.get_data_wiki(filtered_query)

    # Return the differents informations in a JSON format
    return jsonify(query, informations, lat, lng)
