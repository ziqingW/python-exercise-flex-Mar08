import pickle

contacts = {
    "Cersei": {
        "Number": "123-455-7890",
        "Email": "Cersei@kingslanding.com",
        "URL": "www.queen.com"
        },
    "Jaime": {
        "Number": "244-234-3134",
        "Email": "Jaime@kingslanding.com",
        "URL": "www.kingsguard.org"
        },
    "Danny": {
        "Number": "766-908-2356",
        "Email": "Danny@Dothraki.net",
        "URL": "www.truequeenofseven.gov"
        },
    "Jon": {
        "Number": "288-903-2341",
        "Email": "Jon@nightswatch.org",
        "URL": "www.iknownothing.com"
        }
}

def lookup():
    person = input("Who do you want to search? ")
    print("Looking for {}'s entry...".format(person))
    if person in contacts.keys():
        print("Found entry for {}:".format(person))
        for k, v in contacts[person].items():
            print("{}: {}".format(k, v))
    else:
        print("No entry for {}.".format(person))

def setNumber():
    person = input("Who do you want to add? ")
    number = input("Phone number: ")
    email = input("Email address: ")
    url = input("URL address: ")
    contacts[person] = {"Number": number, "Email": email, "URL": url}
    print("Entry stored for {}.".format(person))

def deletePerson():
    person = input("Who do you want to delete? ")
    if person in contacts.keys():
        del contacts[person]
        print("Deleted entry for {}.".format(person))
    else:
        print("No entry for {}.".format(person))
    
def listAll():
    for k, v in contacts.items():
        print("Found entry for {}:".format(k))
        for item, value in v.items():
            print("{}: {}".format(item, value))
        print("")

def saveEntry():
    with open("data.pickle", "wb") as f:
        pickle.dump(contacts, f)
    print("All entries are saved.")

def loadEntry():
    global contacts
    with open("data.pickle", "rb") as f:
        contacts = pickle.load(f)
    print("The phone book is recovered.")
    
while True:
    print("")
    print("Electronic Phone Book")
    print("=" * 20)
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Save entries")
    print("6. Restore saved entries")
    print("7. Quit")
    answer = 0
    if answer not in range(1, 8):
        answer = int(input("What do you want to do (1-7)? "))
    if answer == 1:
        lookup()
    elif answer == 2:
        setNumber()
    elif answer == 3:
        deletePerson()
    elif answer == 4:
        listAll()
    elif answer == 5:
        saveEntry()
    elif answer == 6:
        loadEntry()
    else:
        print("Bye.")
        break