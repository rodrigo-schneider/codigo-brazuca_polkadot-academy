def calcular_bmi(peso, altura):

    if altura <= 0:
        return "A altura deve ser um valor positivo."
    return peso / (altura ** 2)

peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))

bmi = calcular_bmi(peso, altura)

if isinstance(bmi, str):
    print(bmi)
else:
    print(f"O Índice de Massa Corporal (IMC) é {bmi:.2f}.")
