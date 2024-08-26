def contarLetra(frase, letra):
    return frase.lower().count(letra.lower())

frase = input("Digite uma frase: ")
letra = input("Digite a letra que deseja contar: ")

if len(letra) != 1:
    print("Por favor, digite apenas uma letra.")
else:
    quantidade = contarLetra(frase, letra)
    print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")
