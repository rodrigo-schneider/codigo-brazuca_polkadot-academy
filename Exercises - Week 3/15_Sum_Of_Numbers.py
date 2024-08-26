def soma_numeros(n):
    
    if n < 1:
        return "O número deve ser um inteiro positivo."
    return n * (n + 1) // 2

n = int(input("Digite um número inteiro positivo: "))

resultado = soma_numeros(n)
print(f"A soma dos primeiros {n} números naturais é {resultado}.")
