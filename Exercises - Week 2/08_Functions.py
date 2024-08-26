def parOuImpar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número: "))
resultado = parOuImpar(numero)
print(f"O número {numero} é {resultado}.")
