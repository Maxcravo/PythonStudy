import requests # biblioteca que permite que façamos requests, para APIs online GET, POST, PUT, DELETE
import sys
import json # biblioteca que já vem junto com o python e que permite que manipulemos dados Json o que facilita receber e manipular 
            # dados de chamadas Requests recebidos das APIs online

nameBand = ""
music = ""

while nameBand ==  "": 
   nameBand = input("Informe o nome da banda desejada: ")
while music == "": 
   music = input("informe o nome da música desejada: ")

if nameBand and music != "":
  response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+ nameBand)

# print(response.json())

# print(json.dumps(response.json(), indent=2))  # utilizamos a função dump da biblioteca json para facilitar a visualização do resultado da request

# conseguimos iterar ainda mais sobre essa nossa resposta, sabemos que na nossa resposta temos um dicionário chamado results
# conseguimos iterar sobre esse dicionário através de uma estrutura de repetição e buscar apenas pelo item que é interessante para nós. 

resultResponse = response.json()

#* Importante notar como acessamos o dicionário results dentro da nossa response, response["results"], ou seja dentro de response buscamos um objeto com o nome results
for result in resultResponse["results"]: # Aqui acabamos de falar que para cada chave dentro do dicionário chamado results vamos fazer algo
  print(result["trackName"]) # Aqui pontuamos que queremos printar apenas a chave denominada trackName no nosso dicionário results