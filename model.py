import json

'''Simulation of a database. Should not be done like this in actual production. This is just a json file'''

def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)

def save_db():
    with open('flashcards_db.json','w') as f:
        return json.dump(db,f)

db = load_db()