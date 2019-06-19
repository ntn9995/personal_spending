import re
from helper import Helper
from flask import Flask, jsonify, request
from sheets import Sheets
import constants

app = Flask(__name__)

@app.route("/budget/api/email", methods=["POST"])
def processExpense():

	payload = request.json
	parsedReq = parsePayload(payload)

	if not parsedReq:
		return jsonify({
			"success": "false",
			"msg": "illegal request body"
			})

	sheet = Sheets()

	sheet.addExpense(parsedReq["amount"], parsedReq["description"], parsedReq["category"], parsedReq["method"])

	return jsonify({
		"success": "true"
	})

def parsePayload(payload):
	
	if not payload:
		raise None
	
	helper = Helper()

	try:
		amount = helper.parseAmount(payload["amount"])
	except ValueError as e:
		print(e)
		return None
	
	description = payload["description"]
	category = helper.assignCategory(description, constants.CAT_MAP)
	method = "debit"

	return {
		"amount": amount,
		"description": description, 
		"category": category, 
		"method": method
		}
	
if __name__ == '__main__':
	app.run()