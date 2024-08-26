def contar_palavras(frase):
    
    palavras = frase.split()
    return len(palavras)

frase = input("Digite uma frase para contar as palavras: ")

numero_palavras = contar_palavras(frase)
print(f"A frase contém {numero_palavras} palavra(s).")
