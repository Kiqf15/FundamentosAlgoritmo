import os 

def create():
    nome = input('Digite o nome: ')
    sobrenome = input ('Digite o sobrenome:')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    arquivo = open(nome+'_'+sobrenome+'.txt', 'w')
    arquivo.write('%s %s' % (telefone, email))
    arquivo.close()

def read():
    nome = input('Digite o nome: ')
    sobrenome = input ('Digite o sobrenome:')
    arquivo = open(nome+'_'+sobrenome+'.txt', 'r')
    lista = arquivo.readlines()
    print(lista)

def delete():
    nome = input('Digite o nome: ')
    sobrenome = input ('Digite o sobrenome:')
    os.remove(nome+'_'+sobrenome+'.txt', 'r')

def update():
    nome = input('Digite o nome: ')
    sobrenome = input ('Digite o sobrenome:') 
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    arquivo = open(nome+'_'+sobrenome+'.txt', 'w')
    resposta = int(input('Número 0 para mudar todas as opções\nNúmero 1 para mudar o nome\nNúmero 2 para mudar o sobrenome\nNúmero 3 para mudar o telefone\nNúmero 4 para mudar o email\nDigite aqui: '))
    if resposta == 0:
        delete()
        create()
    elif resposta == 1:
        nome = input('Digite o novo nome: ')
        arquivo.write('%s' % (nome))
        arquivo.close()
    elif resposta == 2:
        sobrenome = input('Digite o novo sobrenome: ')
        arquivo.write('%s' % (sobrenome))
        arquivo.close()
    elif resposta == 3:
        telefone = input('Digite o novo telefone: ')
        arquivo.write('%s' % (telefone))
        arquivo.close()
    elif resposta == 4:
        email = input('Digite o novo email: ')
        arquivo.write('%s' % (email))
        arquivo.close()
    
while True: 
    print('Digite 1 para criar\nDigite 2 para procurar\nDigite 3 para deletar\nDigite 4 para update')
    entrada = int(input('Digite a opção: '))
    if entrada == 1:
        create()
    elif entrada == 0:
        break
    elif entrada == 2:
        read()
    elif entrada == 3:
        delete()
    elif entrada == 4:
        update()


