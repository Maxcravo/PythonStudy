def main():
  hello("world")

def hello (name):
  print(f"hello, {name}")

#*main() tg# caso queiramos exportar esse arquivo como um modulo executar o mesmo no arquivo vai fazer com que o arquivo
      # seja executado toda vez que for chamdo em outro arquivo

# para evitar isso usamos essa associação, para evitar que main seja chamada sempre que importada e usada em outro arquivo, 
# essa condição determina que quando main for importada em um arquivo ela não será chamada, pois essa condição só será satisfeita e main
# chamada quando o arquivo for diretamente executado na linha comando/bash 
if __name__ == "__main__":
  main()


