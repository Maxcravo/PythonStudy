# name = input("tell me your name: ")

# print("hello,",name)

# print("testando," "max felipe,", end="") # aqui se visualiza a capacidade de resscrevermos uma funcionalidade padrão do sistema 
# Existe diversos métodos que podemos usar para trabalhar com strings




# test = "testando o métodos de string "
# test = test.capitalize()
# print(test)

# outro teste

# espaco = input("digite seu nome com espaços:")
# espaco = espaco.strip() # NUNCA ESQUECER QUE DEVEMOS declarar o novo valor da nossa variável
# print(f"hello, {espaco}")


# podemos é claro modificar uma string com diversos métodos para mudar o dado de acordo com a necessidade

# formating = input("escreva aqui o seu nome: ")
# formating = formating.strip()
# formating = formating.title()

# print(f"seu nome é {formating}")

# formating = ("      vai ser capitalizado em todas as letras e ter seu espaço em branco removido ")

# formating = formating.strip().title()
# print(formating)

name = input("digite seu nome com espaços:")

name = name.strip().title()

# o split aqui vai dividir as palavras a partir dos espaços em branco
# Aqui vemos que é possível associar 2 variáveis a um único resultado.
# Importante notar que aqui vale a pena tal ato, pois o método split divide o resultado de name em 2 
primeiro, segundo = name.split(" ") 

print(f"olá {segundo}")






