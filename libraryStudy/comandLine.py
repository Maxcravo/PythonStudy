import sys # biblioteca que permite que interajamos diretamente com o sistema

#  # permite que digitemos o nome do usuário antes mesmo do usuário iniciar o programa, passado um argumento junto com a execução do nosso arquivo python 

#* if len(sys.argv) < 2:
#*   print("Faltaram argumentos a serem passdos")
#* elif len(sys.argv) > 2:
#*   print("Foram passados mais argumentos que o suportado")
#* else:
#*   print(f"hello, meu nome é, {sys.argv[1]}")

# aqui usamos o if else para prever os possíveis nomes

# podemos usar funções da própria bibliotea sys para tratarmos nossos erros

if len(sys.argv) < 2:
  sys.exit("Faltaram argumentos a serem passdos")
elif len(sys.argv) > 2:
  sys.exit("Foram passados mais argumentos que o suportado")
else:
  print(f"hello, meu nome é, {sys.argv[1]}")