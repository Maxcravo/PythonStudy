from testingInPython.mainFunc import square


# agora criemos uma função para testar nossa outra função criada

def main():
    test_square()

# usamos para testar a palavra reservada assert que, que basicamente define que é algo deve obrigatóriamente ser true 
# usando juntamente com a estrutura try except conseguimos fazer com que nosso código identifique erros e tenham logs user friendly sobre eles
def test_square():
    try:
      assert square(2) == 4
    except AssertionError:
      print(f"a operação square(2), não atingiu o resultado esperado")
    try:
      assert square(3) == 9
    except AssertionError:
      print(f"a operação square(3), não atingiu o resultado esperado")


if __name__ == "__main__":
  main()