import re
from flask import Flask, jsonify, request
from sheets import Sheets
import constants
import email_parser

app = Flask(__name__)

@app.route("/budget/api/email", methods=["POST"])

def parseEmail():
    payload = request.json
    amount = payload["amount"]
    description = payload["description"]
    
    print("{} - {}".format(amount, description))

    return jsonify({
        "success": "true",
        "amount": amount,
        "description": description
        })



if __name__ == '__main__':
    app.run()