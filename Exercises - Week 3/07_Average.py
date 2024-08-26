def calcular_media():

    notas = []
    
    while True:
        nota = float(input("Digite uma nota (ou -1 para terminar): "))
        
        if nota == -1:
            break
        
        if nota >= 0:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, insira uma nota não negativa.")
    
    if notas:
        media = sum(notas) / len(notas)
        return media
    else:
        return "Nenhuma nota válida foi inserida."

media_notas = calcular_media()
print(f"A média das notas é: {media_notas}")
