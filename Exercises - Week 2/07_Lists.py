listaCompras = []

while True:
    item = input("Digite um item para a lista de compras ou digite 'fim' para terminar: ")
    
    if item.lower() == 'fim':
        break
    
    listaCompras.append(item)

print("\nSua lista de compras completa é: ")
for i, item in enumerate(listaCompras, 1):
    print(f"{i}. {item}")
