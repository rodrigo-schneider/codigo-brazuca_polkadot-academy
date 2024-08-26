def contar_vogais(frase):

    vogais = "aeiou"
    contagem = 0
    frase = frase.lower()
    
    for letra in frase:
        if letra in vogais:
            contagem += 1
            
    return contagem

frase = input("Digite uma frase para contar a(s) vogal(is): ")

total_vogais = contar_vogais(frase)
print(f"A frase contém {total_vogais} vogal(is).")
