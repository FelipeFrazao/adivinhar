import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")


def define_palavra_secreta(nome_arquivo = "palavras.txt"):
    palavras = []

    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].lower()
    return palavra_secreta


def define_letras_acertadas(palavra):
    return ["_" for i in palavra]


def pega_chute():
    chute = input("Qual letra? ").lower().strip()
    return chute


def exibe_acerto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def verifica_acertos(letras_acertadas):
    print(letras_acertadas)
    letras_faltando = str(letras_acertadas.count('_'))
    print('Ainda faltam acertar {} letras'.format(letras_faltando))
    return letras_faltando


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if (tentativas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    palavra_secreta = define_palavra_secreta()
    letras_acertadas = define_letras_acertadas(palavra_secreta)

    tentativas = 7

    while (tentativas > 0):
        print("Você tem {} tentativas use-as com cuidado".format(tentativas))
        chute = pega_chute()
        if (chute in palavra_secreta):
            exibe_acerto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas -= 1
            desenha_forca(tentativas)
            if (tentativas == 0):
                mensagem_perdedor(palavra_secreta)

        letras_faltando = verifica_acertos(letras_acertadas)
        if (int(letras_faltando) == 0):
            mensagem_ganhou()
            break


if (__name__ == "__main__"):
    jogar()
