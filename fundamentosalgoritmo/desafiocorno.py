def palavra():
    palavra = input("Digite a palavra secreta:")
    return palavra
    
def carrega_palavra():
    palavra = []
    with open("palavra.txt", "w", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavra.append(linha)
    return palavra
    arquivo.close()

def letra_acertada(palavra):
    return ("-" for letra in palavra)
    print(palavra)

def chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, letra_acertada, palavra):
    i = 0
    for letra in palavra:
        if (chute == letra):
            letra_acertada[i] = letra
        i += 1

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

    palavra()

    letra_acertada(palavra)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letra_acertada(palavra))
    print(letra_acertada)
    
    while (not acertou and not enforcou):

        chute = chute()

        if (chute in palavra):
            chute_correto(chute, letra_acertada, palavra)
            letras_faltando = str(letra_acertada.count("-"))
            if (letras_faltando == "0"):
                print(palavra.upper())
                print("Você acertou!")
        else:   
            erros += 1
            print(letra_acertada)
            forca(erros)
        
        enforcou == erros == 5
        acertou = "-" not in letra_acertada

jogar()