def inverter_string(s):
    
    return s[::-1]

entrada = input("Digite uma string para ser invertida: ")

string_invertida = inverter_string(entrada)
print(f"A string invertida é: {string_invertida}")
