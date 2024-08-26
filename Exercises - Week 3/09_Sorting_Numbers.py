def ordenar_numeros(a, b, c):

    return tuple(sorted([a, b, c]))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros_ordenados = ordenar_numeros(num1, num2, num3)
print(f"Os números em ordem crescente são: {numeros_ordenados}")
