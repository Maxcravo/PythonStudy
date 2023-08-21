print("faça certo calculos")
print("primeiro calculo a divisão de 145 por 23: ")
print("agora calcule a multiplicação de 24 vezes 90:" )

firstnum = input("dê os valor do primeiro número:")
secundnum = input("dê o valor do seguindo número: ")

select =  input("digite 1 para calcular a divisão e 2 para calcular a multiplicação")
select = int(select)

firstnum = float(firstnum)
secundnum = float(secundnum)

if select ==  1:
  result = firstnum /  secundnum
elif select == 2:
  result = firstnum * secundnum

result = round(result, 2) # função round apróxima o resultado para o inteiro mais próximo

print(f"O resultado é: {result}")

# outra forma de obter o mesmo resulta seria o de usar uma função dentro de outra função

# firstnum = int(input("digite o primeiro número"))
# secundnum = int(input("digite o segundo número"))