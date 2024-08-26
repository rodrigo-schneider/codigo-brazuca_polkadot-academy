lista_compras = []

while True:
    item = input("Digite um item para a lista de compras ou digite 'fim' para terminar: ")
    
    if item.lower() == 'fim':
        break
    
    lista_compras.append(item)

print("\nSua lista de compras completa é: ")
for i, item in enumerate(lista_compras, 1):
    print(f"{i}. {item}")
