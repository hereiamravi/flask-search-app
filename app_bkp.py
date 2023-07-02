# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    query = ''
    results = []
    html = ''
    if request.method == 'POST':
        # get the query from the form
        query = request.form.get('query')
        # perform a web search using the query
        response = requests.get('https://www.google.com/search?q=' + query)
        # check the content type of the response
        # print(response.content)
        print(response.headers)
        if response.headers['Content-Type'] == 'application/json':
            # parse the response as JSON
            data = response.json()
            # extract the web results from the data
            results = data['webPages']['value']
            return render_template('index.html', query=query, results=results)
        elif 'text/html' in response.headers['Content-Type']:
            print("abcd")
            html = response.text
            return render_template('index.html', query=query, html=html)
        else:
            # handle other formats or raise an error
            return render_template('error.html', message='The response is not in correct format')
    return render_template('index.html', query=query, results=results, html=html)

@app.errorhandler(404)
def page_not_found(e):
    # handle 404 errors
    return render_template('error.html', message='Page not found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # handle 500 errors
    return render_template('error.html', message='Internal server error'), 500

if __name__ == '__main__':
    app.run(debug=True)
