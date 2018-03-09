import json

contacts = {
    "Li"
    "Jimmy": "244-234-3134",
    "Danny": "766-908-2356",
    "Jon": "288-903-2341"
}

def lookup():
    person = input("Whose number do you want to know? ")
    print("{}'s number is {}".format(person, contacts[]))