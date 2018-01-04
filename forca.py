import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].lower()
    letras_acertadas = ["_" for i in palavra_secreta]
    tentativas = len(palavra_secreta)

    jogando = True
    while (tentativas > 0):
        print("Você tem {} tentativas use-as com cuidado".format(tentativas))
        chute = input("Qual letra? ").lower().strip()
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta.strip():
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas -= 1
            if (tentativas == 0):
                print("Você perdeu")

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        if (int(letras_faltando) == 0):
            print("Parabéns voce ganhou!!")
            break

if (__name__ == "__main__"):
    jogar()
