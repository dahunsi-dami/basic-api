#!/bin/env/python3
"""A public API to `tap` my HNG 12 internship info."""

from datetime import datetime
from flask import Flask, Response
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def get_info():
    """
    Defines logic to return current time with-
    -hardcoded email and github repo URL.
    """

    anointing = {
        "email": "gbemigadare@gmail.com",
        "current_datetime": datetime.now().replace(microsecond=0).isoformat() + 'Z',
        "github_url": "https://github.com/dahunsi-dami/basic-api-py"
    }

    receiveIT = json.dumps(anointing)
    return Response(receiveIT, mimetype='application/json'), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
