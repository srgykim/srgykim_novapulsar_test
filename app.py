from flask import Flask

import pandas as pd
import os

DEBUG = True
HOST = '10.2.0.4'
PORT = 8000

app = Flask(__name__)


@app.route('/api/v1/claims_test')
def hello_world():
    path = os.path.join(os.path.dirname(__file__), 'static/claims_test.csv')
    df = pd.read_csv(path)
    return df.to_json(orient='table')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
