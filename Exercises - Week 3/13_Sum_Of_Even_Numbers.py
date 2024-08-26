def soma_numeros_pares(inicio, fim):
    
    soma = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma += numero
    return soma

inicio_intervalo = 1
fim_intervalo = 100

soma_pares = soma_numeros_pares(inicio_intervalo, fim_intervalo)
print(f"A soma de todos os números pares entre {inicio_intervalo} e {fim_intervalo} é {soma_pares}.")
