segredo = input("Digite a palavra secreta:")
letra = "-"*len(segredo)
listar = list(letra)

def forca(erros):
    print("X==:==")
    print("X  :  ")

    if (erros == 1):
        print("X  O  ")
        print("X     ")
        print("X     ")
        print("X     ")
    if (erros == 2):
        print("X  O  ")
        print("X  |  ")
        print("X     ")
        print("X     ")
    if (erros == 3):
        print("X  O  ")
        print("X \|  ")
        print("X     ")
        print("X     ")
    if (erros == 4):
        print("X  O  ")
        print("X \|/ ")
        print("X /   ")
        print("X     ")
    if (erros == 5  ):
        print("X  O  ")
        print("X \|/ ")
        print("X / \ ")
        print("X     ")

    print("===========")


def jogar():
    enforcou = False
    acertou = False
    erros = 0
    chute = input("Digite uma letra:").lower()
    
    print(letra)

    while (not acertou or not enforcou):
        pass
