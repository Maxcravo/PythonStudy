characters = {
  "aragorn": "filho de arathorn",
  "Frodo": "portador do um anel",
  "sam": "fiel escudeiro",
  "golum": "aficcionado pelo anel",
}
# usando métodos para recuperar dados da lista
print(characters.get("sam"))

# caso queiramos iterar sobre as chaves do dicionário
for character in characters:
  print(character)

# caso queiramos iterar sobre tanto a chave quanto o valor
for character in characters:
  print(character, characters[character])


#! podemos querer ter um dicionário com diversas informações sobre um elemento do sistema, para isso podemos ter uma lista de dicionarios

Lotr= [
	{"nome": "frodo", "item": "anel","ajudante": "sam"},
	{"nome": "aragorn", "item": "espada", "ajudante": "gandalf" },
	{"nome": "legolas", "item": "arco", "ajudante": "gimli" },
]

for character in Lotr:
    print(f'{character["nome"]},{character["item"]},{character["ajudante"]}',sep="" )

