import re
from flask import Flask, jsonify, request
from sheets import Sheets
import constants
import email_parser

app = Flask(__name__)

@app.route("/budget/api/email", methods=["POST"])

def parseEmail():
    payload = request.json
    body = payload["body"]
    subject = payload["subject"]
    sheet = Sheets()
    print(repr(body))

    description, amount, category, method = parseEmail.parseEmail(subject, body)
    
    if amount and method:
        Sheets.addExpense(amount, description, category, method)
        


if __name__ == '__main__':
    app.run()