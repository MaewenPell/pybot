from flask import Flask, render_template, request
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
    print(query)
    filtered_query = parser.filter_words(query)
    print(filtered_query)
    return render_template('index.html', filtered_query=filtered_query)
