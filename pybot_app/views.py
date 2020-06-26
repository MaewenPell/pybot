from flask import Flask, render_template, request
from .actions.parsing import Parser

app = Flask(__name__)
parser = Parser()


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.get_data(as_text=True)
    if parser.is_stop_words(data):
        print("Stop word")
    else:
        print('Not a stop word')

    return render_template('index.html')
