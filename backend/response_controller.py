from flask import Flask, jsonify
from backend.database.database_api import *

app = Flask(__name__)


@app.route('/json/projects')
def projects():
    return get_json_response_from_query(get_projects())


# Utility Methods

def get_json_response_from_query(query_obj):
    return jsonify([row.serialize for row in query_obj])

# run server


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)