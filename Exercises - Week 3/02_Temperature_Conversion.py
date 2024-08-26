def converter_temperatura(celsius):

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit, kelvin = converter_temperatura(temperatura_celsius)
print(f"A temperatura de {temperatura_celsius}°C é igual a {fahrenheit}°F e {kelvin} K.")
