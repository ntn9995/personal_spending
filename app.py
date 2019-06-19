import re
from flask import Flask, jsonify, request
from sheets import Sheets
import constants
import parser

app = Flask(__name__)

@app.route("/budget/api/email", methods=["POST"])
def parseExpense():
    payload = request.json
    amount = payload["amount"]
    description = payload["description"]
    category = parser.assignCategory(description, constants.CAT_MAP)
    method = "debit"

    Sheets.addExpense(amount, description, category, method)

    return jsonify({
        "success": "true"
        })



if __name__ == '__main__':
    app.run()