# criando uma função básica 

# def hello ():
#     print("hello word") # corpo da função

# hello() # aqui chamamos a função

# uma função também deve conseguir receber paramêtros\
from tokenize import Number


def hello(to="mundo"):
  print(f"hello, {to}" ) # aqui vamos printar hello e mais o valor do nosso parâmetro recebido na função

hello() # aqui definimos que vamos chamar nossa função name e vamos passar como parametro 
#             a essa função o input definido a cima 

# aqui criamos uma função chamada name, e dentro dela chamamos nossa função hello, 
# hello é chamada dentro da nossa função main
def main():
  name = input("qual seu nome: ")
  hello(name)

main()

def main():
  number = int(input("digite o valor de x: "))
  print(f"o valor de x elevado ao quadrado é {square(number)}")

def square(x):
  return x * x

main()


