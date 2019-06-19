import re
from flask import Flask, jsonify, request
from sheets import Sheets
from parser import Parser
import constants


app = Flask(__name__)

@app.route("/budget/api/email", methods=["POST"])
def processExpense():
    payload = request.json
    parser = Parser()

    amount = payload["amount"]
    description = payload["description"]
    category = parser.assignCategory(description, constants.CAT_MAP)
    method = "debit"

    sheet = Sheets()
    sheet.addExpense(amount, description, category, method)

    return jsonify({
        "success": "true"
        })



if __name__ == '__main__':
    app.run()