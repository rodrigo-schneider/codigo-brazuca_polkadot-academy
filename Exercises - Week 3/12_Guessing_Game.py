import random

def jogo_adivinhacao():
    
    numero_aleatorio = random.randint(1, 100)  # Escolhe um número aleatório entre 1 e 100
    tentativas = 0
    adivinhou = False
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while not adivinhou:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1
        
        if tentativa < numero_aleatorio:
            print("O número é maior.")
        elif tentativa > numero_aleatorio:
            print("O número é menor.")
        else:
            adivinhou = True
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")

jogo_adivinhacao()
