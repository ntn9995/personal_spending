import re
from helper import Helper
from flask import Flask, jsonify, request
from sheets import Sheets
import constants

app = Flask(__name__)

@app.route("/budget/api/email", methods=["POST"])
def processExpense():
    payload = request.json
    helper = Helper()

    amount = payload["amount"]
    description = payload["description"]
    category = helper.assignCategory(description, constants.CAT_MAP)
    method = "debit"

    sheet = Sheets()
    sheet.addExpense(amount, description, category, method)

    return jsonify({
        "success": "true"
        })

if __name__ == '__main__':
    app.run()