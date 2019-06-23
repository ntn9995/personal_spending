import re

class Helper:

	def parseAmount(self, amountStr):
		regex = '\$ ?[\d\.]{3,7}'
		amount = extract(regex,amountStr)
		if amount:
			return amount
		raise ValueError

	def assignCategory(self, description, mapping):
		category = "Other Expenses"
		for key in mapping:
			if key in description.lower():
				category = mapping[key]
				break

		return category

def extract(regex, s):
	res = re.search(regex, s)
	return None if not res else res.group()