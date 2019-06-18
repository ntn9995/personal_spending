import re
import constants

def parseEmail(subject, body):

    description, amount, category, method = ''

    if "You paid" in subject:
        description, amount = parseVenmo(body, "You paid")
        category = assignCategory(description, constants.VENMO)
        method = "Venmo"

    elif "charge request" in subject:
        description, amount = parseVenmo(body, "charge requst")
        category = assignCategory(description, constants.VENMO)
        method = "Venmo"
     

    elif "Debit card used" in subject:
        description, amount = parseBofA(body)
        category = assignCategory(description, constants.BOFA)
        method = "BofA"

    return description, amount, category, method
    
def parseVenmo(body, subject="You paid"):

    description = \
        extract("(?<=\) \\n \\n)(.*)(?= \\n \ T)", body)\
        if subject == "You paid" else \
        extract("(?<=\-5\) \\n \\n)(.*)(?= \\n  T)", body)
    
    amount = extract("(?<=\- \$)(.*)(?= \\n     \\n  L)", body)

    return description, amount

def parseBofA(body):
    description = "bank of america, food"
    amount = "$5.00"
    return description, amount

def extract(regex, body):
    result = re.search(regex, body)
    return "NOT FOUND" if not result else result.group()

def assignCategory(description, mapping):

    category = "NOT FOUND"

    for key in mapping:
        if key in description.lower():
            category = mapping[key]
            break

    return category