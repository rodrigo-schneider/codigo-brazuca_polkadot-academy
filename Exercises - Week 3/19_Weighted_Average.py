def calcular_media_ponderada(nota1, nota2, nota3):

    peso1 = 2
    peso2 = 3
    peso3 = 5
    
    soma_ponderada = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    soma_pesos = peso1 + peso2 + peso3
    
    return soma_ponderada / soma_pesos

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_ponderada = calcular_media_ponderada(nota1, nota2, nota3)
print(f"A média ponderada das notas é: {media_ponderada:.2f}")
