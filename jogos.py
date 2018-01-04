import adivinhacao
import forca

print("*********************************")
print("***Escolha um jogo***")
print("*********************************")

print("1 Adivinhação 2 Forca")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Adivinhacao")
    adivinhacao.jogar()
elif(jogo == 2):
    forca.jogar()
