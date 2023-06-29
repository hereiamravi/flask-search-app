# app.py
import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    query = ''
    results = []
    auth_key = os.environ['AUTH_KEY']
    # headers = {"Authorization": "Bearer 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"}
    headers = {"Authorization": f"Bearer {auth_key}"}
    if request.method == 'POST':
        # get the query from the form
        query = request.form.get('query')
        inputs = {
            'inputs':query
        }
        # perform a web search using the query
        response = requests.post('https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions',headers=headers,json=inputs)
        # check the content type of the response
        if response.headers['Content-Type'] == 'application/json':
            # parse the response as JSON
            results = response.json()[0]
        else:
            # handle other formats or raise an error
            return render_template('error.html', message='The response is not in correct format')
    return render_template('index.html', query=query, results=results)

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
