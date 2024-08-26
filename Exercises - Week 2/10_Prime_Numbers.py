def numeroPrimo(numero):

    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrarPrimos(intervalo_inicio, intervalo_fim):

    print(f"Números primos no intervalo de {intervalo_inicio} a {intervalo_fim}:")
    for numero in range(intervalo_inicio, intervalo_fim + 1):
        if numeroPrimo(numero):
            print(numero)

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio > fim:
    print("O início do intervalo deve ser menor ou igual ao fim do intervalo.")
else:
    encontrarPrimos(inicio, fim)
