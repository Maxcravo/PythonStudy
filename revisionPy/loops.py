# i = 0

# while i != 5:
#   i = i + 1
#   print("ai zé da manga")

 # aqui dizemos que x vai começar do valor 0 e vai até o valor 3, enquanto x
 # não tiver o valor 3, o programa irá executar o código abaixo
# for x in range(0,3):
# 	print(f"o valor de x atual é: {x}")

from threading import Timer
# outra forma de importar biblioteca é:


def printdefault():
  print("ai zé")

def printar(x):
   time = Timer(x, printdefault)
   time.start()

def timer():
  x = int(input("digite o valor de x"))
  while x <= 0:
    x = int(input("degite o valor de x'"))
  if x > 0: # definimos se caso o x chegar a ser maior que 0 ele retorna x
    for i in range(1,10):
     time = Timer(i, printar(x))
     time.start()
        

timer()