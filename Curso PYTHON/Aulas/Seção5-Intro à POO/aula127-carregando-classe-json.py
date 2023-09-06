import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def load_person_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        person = Person(**data)
        return person

loaded_person = load_person_from_json('person.json')
print(f"Nome: {loaded_person.name}, Idade: {loaded_person.age}")
