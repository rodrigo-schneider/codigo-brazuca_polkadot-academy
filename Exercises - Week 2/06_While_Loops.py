soma = 0

while True:
    numero = int(input("Digite um número ou digite 0 para terminar: "))
    
    if numero == 0:
        break  
    
    soma += numero

print("A soma dos números digitados é: ", soma)