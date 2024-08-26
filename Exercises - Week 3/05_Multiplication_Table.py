def exibir_tabuada(numero):

    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para exibir a tabuada: "))

exibir_tabuada(numero)
