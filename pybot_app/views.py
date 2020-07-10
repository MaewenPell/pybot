from flask import Flask, render_template, request, jsonify
from .actions.parsing import Parser


app = Flask(__name__)

# Import config options
app.config.from_object('config')
parser = Parser(app.config['MAPS_API_KEY'])


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
    query = request.get_data(as_text=True)
    filtered_query = parser.filter_words(query)
    return jsonify(query)
