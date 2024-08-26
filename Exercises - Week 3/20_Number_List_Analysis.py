def analisar_lista_numeros(lista):
    
    if not lista:
        return None, None, None
    
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    
    return maior, menor, media

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(float, entrada.split()))

maior, menor, media = analisar_lista_numeros(numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A média dos números é: {media:.2f}")
