# agora usemos um modulo para conseguirmos fazer nossos testes, de forma mais automatizada, 
# evitando criar muito código de teste repetido.
import pytest

from mainFunc import square

# usando rodando o código com pytest ao inves de python conseguiremos usar o pytest para nos dar logs de erros
# sem precisar que manualmente precisemos usar try exception com print, automatizando e agilizando o processo.
def test_squere():
    assert square(2) == 4
    assert square(3) == 9

# uma forma de melhorar a captação de erros usando o pytest é dividir as funções de test em pequenas funções que
# buscam por erros de natureza diferente

# para utilizar o pytest para tal é necessário que rodemos nosso código utilizando o comando pytest

def test_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_zero():
  assert square(0) == 0
  
def test_str():
   with pytest.raises(TypeError):
        square("cat")