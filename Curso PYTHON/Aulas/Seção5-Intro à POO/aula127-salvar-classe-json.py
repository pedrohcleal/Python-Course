# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Joao", 30)

person_dict = vars(person)  # Converte a instância para um dicionário

print(person_dict, **person)

with open('person.json', 'w', encoding='utf8') as json_file:
    json.dump(person_dict, json_file)
