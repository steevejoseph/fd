from flask import Flask, json, g, Response, request, render_template

# from flask_cors import CORS
import requests

application = Flask(__name__)
# CORS(application)


@application.route('/', methods=['GET'])
def index():
    return "Welcome to the API"


if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
