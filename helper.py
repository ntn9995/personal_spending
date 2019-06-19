class Helper:

	def assignCategory(self, description, mapping):
		category = "NOT FOUND"
		for key in mapping:
			if key in description.lower():
				category = mapping[key]
				break

		return category