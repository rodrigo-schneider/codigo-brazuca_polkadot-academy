def calculadora(num1, num2, operacao):

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: Divisão por zero."
        return num1 / num2
    else:
        return "Operação inválida."

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

resultado = calculadora(num1, num2, operacao)
print(f"O resultado da operação é: {resultado}")
