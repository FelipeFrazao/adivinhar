
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = "aranha"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    jogando = True
    while(jogando):
        chute = input("Qual letra? ").strip()
        index = 0
        for letra in palavra_secreta.strip():
            if(chute.lower() == letra.lower()):
                letras_acertadas[index] = letra
            index += 1

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print( 'Ainda faltam acertar {} letras'.format(letras_faltando))
        if(int(letras_faltando) == 0):
            jogando = False
            print("Parabéns voce ganhou!!")

if(__name__ == "__main__"):
    jogar()