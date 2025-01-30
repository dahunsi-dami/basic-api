#!/bin/env/python3
"""A public api to retrieve HNG 12 internship details."""

from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

@app.route('/api/info', methods=['GET'])
def get_info():
    """
    Defines logic to return current time with-
    -hardcoded email and github repo URL.
    """
    heeMail = "gbemigadare@gmail.com"
    geetLink = "https://github.com/dahunsi-dami/basic-api"
    timeNowNow = datetime.now().replace(microsecond=0).isoformat() + 'Z'

    receiveIT = {
        "email": heeMail,
        "current_datetime": timeNowNow,
        "github_url": geetLink
    }

    return jsonify(receiveIT), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
