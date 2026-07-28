import random

# Declarando variáveis para gerar um número aleatório entre 1 e 100 e controlar o número de tentativas
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Tente um número maior.")
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        acertou = True
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")