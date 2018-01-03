import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_screto = round(random.randrange(1,101))
tentativas = 0

print("Selecione um nivel de dificuldade")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Nivel de dificuldade: "))

if nivel == 1:
    tentativas = 15
elif nivel == 2:
    tentativas = 10
else:
    tentativas = 5

while (tentativas > 0):

    print("Você tem {} tentativas use-as com cuidado".format(tentativas))
    print("")
    chute = input("Digite um número entre 1 e 100: ")
    print("")
    chute_int = int(chute)
    if (chute_int < 1 or chute_int > 100):
        print("Por favor, digite um número entre 1 e 100!")
        continue

    acertou = chute_int == numero_screto
    maior = chute_int > numero_screto
    menor = chute_int < numero_screto

    if (acertou) :
        print("Parabéns voce ganhou o jogo!")
        break
    else:
        if (maior):
            print("Errou, seu chute foi maior que o número")
            print("")
        elif(menor):
            print("Errou, seu chute foi menor que o número")
            print("")
        tentativas -=1

if (tentativas == 0):
    print("Você perdeu")