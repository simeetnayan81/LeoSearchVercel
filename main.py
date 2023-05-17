# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template, request
from utils.perform_search import sem_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    results = sem_search(query)  #Replace with your search logic
    return render_template('results.html', query=query, results=results)



if __name__ == '__main__':
    app.run()
