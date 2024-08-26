def gerar_fibonacci(n):

    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

n = int(input("Digite o número de elementos da sequência de Fibonacci: "))

sequencia_fibonacci = gerar_fibonacci(n)
print(f"Os primeiros {n} números da sequência de Fibonacci são: {sequencia_fibonacci}")
