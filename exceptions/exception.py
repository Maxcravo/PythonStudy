# try:
#   # aqui existe a chance do usuário colocar uma string ao invés de um int
#   # para lidarmos com isso podemos usar o try-catch
#   x = int(input("informe o valor de x: "))
#   print(f"o valor de x é {x}")

# except ValueError:
#   print("o valor digitado não é um inteiro")

# def main():
#   x = getInt() # aqui associamos a variável x o valor que retorna da função getInt
#   print(f"o valor de x é {x}")

# def getInt():
#   while True:
#     try:
#       x = int(input("digite o valor de x: "))
#     except ValueError:
#         print("x não é um inteiro")
#     else: break 
#   return x

# main()


def main():
  x = getInt() # aqui associamos a variável x o valor que retorna da função getInt
  print(f"o valor de x é {x}")

def getInt():
  while True:
    try:
      x = int(input("digite o valor de x: "))
      return x
    except ValueError:
        pass # aqui definimos que mesmo encontrando o ValueError não vamos parar nosso programa 

main()