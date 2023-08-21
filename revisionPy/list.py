# for i in range(0,10):
#   print("meow")

# # caso no contexto do programa não seja necessário específicar a variável
# # que está sendo iterada, é normal que essa variável seja declarada simplesmente
# # pelo "_" 

# for _ in range(10):
#   print("ai zé")

# aqui estamos multiplicando um print por 3, ao fim de cada print
# pulamos para a linha de baixo e definimos que no final do print não deverá pular nenhuma linha
# print("ai zé \n" * 3, end="")

personagens = ["frodo","sam", "aragorn", "pinpim", "legolas"]

# printamos cada elemento dentro da lista de personagem, cabe visualizar que o python automaticamente infere que a variável "personagem" corresponde a cada elemento da lista
# for personagem in personagens:  
# 	print(personagem)

for i in range(len(personagens)):
  print(f"{i} - {personagens[i]}")
