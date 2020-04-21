from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.database.database_api import get_data

app = Flask(__name__)
# allows requests from all other sites
CORS(app)


@app.route('/api')
def projects():
    return jsonify(get_data(request.args))

# run server


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)