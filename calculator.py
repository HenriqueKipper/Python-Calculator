print("Calculadora maneira")

print("Escolha um numero da tabela de calculo entre as opções")

print("1.Adição")

print("2.Subtraçção")

print("3.Multiplicação")

print("4.divisão")

escolha = int(input("Escolha: "))

valor1 = float(input("Primeiro numero: "))

valor2 = float(input("Segundo numero: "))

if escolha == 1:
    soma = valor1 + valor2

    print(f'resultado: {soma}')
elif escolha == 2:
    diferença = valor1 - valor2

    print(f'resultado: {diferença}')
elif escolha == 3:
    produto = valor1 * valor2

    print(f'resultado: {produto}')
elif escolha == 4:
    quociente = valor1 / valor2

    print(f'resultado: {quociente}')

else:
    print("Erro: Opção errada")