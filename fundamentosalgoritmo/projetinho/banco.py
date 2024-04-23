#importar o sistema operacional para encontrar o path do arquivo criado
import os
# biblioteca para ver Data, Horário e Mês
from datetime import datetime

# função para criar um novo usuário
def Novo():
    # chamar a variavel para saber o dia 
    dia = datetime.now()
    # var para gravar o CPF 
    cpf = input('Digite o CPF: ')
    # não continuar o código em caso do CPF já está registrado
    if os.path.isfile(cpf+'.txt'):
        # mensagem que aparece para este caminho
        print('Cliente já registrado!')
    # caso não esteja criado ainda
    else:
        # var que armazena o nome
        nome = input('Digite o nome: ')
        # var que armazena o tipo da conta
        conta = input('Digite o tipo da conta(S, C, P): ')
        # var para armazena o tipo da senha
        senha = input('Digite a senha do usuário: ')
        # var para armazenar o valor inicial
        valorI = float(input('Digite o valor inicial da conta: '))
        # criação de um arquivo para manter essas informações em um lugar
        arquivo = open(cpf+'.txt', 'w')
        # armazena na posição [0]
        arquivo.write('Nome: %s\n' % nome)
        # armazena na posição [1]
        arquivo.write('CPF: %s\n' % cpf)
        # armazena na posição [2]
        arquivo.write('Conta: %s\n' % conta)
        # armazena na posição [3]
        arquivo.write('Senha: %s\n' % senha)
        # forma de mostrar para na função do Extrato (posição [4])
        arquivo.write('Data:{0} + 0 Tarifa: 0.00 Saldo: {1:.2f} \n'.format(dia.strftime('%Y-%m-%d %h %H:%M'), valorI))
        # fechar o arquivo
        arquivo.close()
        # mensagem que aparecerá na tela
        print('Conta criada com êxito!')


# função para apagar um usuário
def Apaga():
    # var para o user digitar o CPF
    cpf = input('Digite o CPF: ')
    # condição para checar se o CPF existe
    if os.path.isfile(cpf+'.txt'):
        # var para digitar a senha
        senha = input('Digite a senha do usuário: ')
        # abrir o arquivo em forma de leitura
        arquivo = open(cpf+'.txt', 'r')
        # criação de uma lista[]
        lista = []
        # var para ler o arquivo
        leitor = arquivo.readlines()
        # fechar o arquivo
        arquivo.close()
        # for para organizar o modo para ler o arquivo
        for x in leitor:
            # var para tirar o \n dentro da lista
            organiza = x.split()
            # guardar os dados, já organizados, em ordem dentro da lista
            lista.append(organiza)
        # condição de segurança
        if lista[1][1] == cpf and lista [3][1] == senha:
            # code para remover o arquivo  criado
            os.remove(cpf+'.txt')
            # mensagem que aparecerá na tela
            print('Conta apagada com êxito!')
        # condição para caso errar a senha
        elif lista[3][1] != senha:
            # mensagem respondendo a condição
            print('Senha incorreta, favor insirir uma senha válida!')
        # fechar o arquivo
        arquivo.close()
    # condição caso erre o CPF
    else:
        # mensagem para a condição
        print('Acho que até os professores erram os números kk')

# função para Debitar
def Debita():
    # variavel para gravar o dia na compra
    dia = datetime.now()
    # var para o user digitar o CPF
    cpf = input('Digite o CPF: ')
    # condição para encontrar o arquivo pelo CPF
    if os.path.isfile(cpf+'.txt'):
        # var para o user digitar a senha
        senha = input('Digite a senha do usuário: ')
        # abrir o arquivo em modo de leitura
        arquivo = open(cpf+'.txt', 'r')
        # criar uma lista
        lista = []
        # var para ler o arquivo
        leitor = arquivo.readlines()
        # fechar o arquivo
        arquivo.close()
        # for para organizar a leitura do arquivo
        for x in leitor:
            # var para tirar o \n da lista
            organiza = x.split()
            # guardar os dados, já organizados, em ordem dentro da lista
            lista.append(organiza)
        # condição de segurança
        if lista[1][1] == cpf and lista [3][1] == senha:
            # var para o user digitar o valor da compra
            compra = float(input('Digite o valor a ser debitado: R$'))
            # condição para a conta tipo Salário
            if  lista[2][1]== 'S':
                # realizar a conta do novo Saldo
                lista[-1][-1] = float(lista[-1][-1]) - compra*1.05
                # condição para certificar que o cliente possa realizar a compra
                if  lista[-1][-1] < 0:
                    # mensagem que aparece para a condição
                    print('Saldo não suficiente!')
                # condição caso o user possa realizar a compra 
                else: 
                    # var para realizar a conta da tarifa do banco
                    tarifa =  compra*0.05
                    # abrir o arquivo em modo APPEND
                    arquivo = open(cpf+'.txt', 'a')
                    # escrever sempre a nova compra em baixo da anterior para criar uma espécie de histórico das compras
                    arquivo.write(('Data:{0} - {1:.2f} Tarifa:{2:.2f} Saldo: {3:.2f} \n'.format(dia.strftime('%Y-%m-%d %h %H:%M'), compra, tarifa, lista[-1][-1])))
                    # fechar o arquivo
                    arquivo.close()
            # condição para a conta tipo Comum
            elif lista[2][1] == 'C':
                # realizar a conta para o novo saldo
                lista[-1][-1] = float(lista[-1][-1]) - compra*1.03
                # condição para que o user possa realizar a compra
                if float(lista[-1][-1]) >= -500:
                    # var para a conta da tarifa do banco
                    tarifa = compra*0.03
                    # abrir o arquivo em modo APPEND
                    arquivo = open(cpf+'.txt', 'a')
                    # escrever sempre a nova compra em baixo da anterior para criar uma espécie de histórico das compras
                    arquivo.write(('Data:{0} - {1:.2f} Tarifa:{2:.2f} Saldo: {3:.2f} \n'.format(dia.strftime('%Y-%m-%d %h %H:%M'), compra, tarifa, lista[-1][-1])))
                    # fechar o arquivo
                    arquivo.close()
                # condição em caso do user não poder realizar a compra
                else:
                    # mensagem para a condição
                    print('Saldo não suficiente!')
            # condição para a conta tipo Plus
            elif lista[2][1] == 'P':
                # realizar a conta para o novo saldo
                lista[-1][-1] = float(lista[-1][-1]) - compra*1.01
                # condição para realizar a compra
                if float(lista[-1][-1]) >= -5000:
                    # var para a conta da tarifa do banco
                    tarifa = compra*0.01
                    # abrir o arquivo em modo APPEND
                    arquivo = open(cpf+'.txt', 'a')
                    # escrever sempre a nova compra em baixo da anterior para criar uma espécie de histórico das compras
                    arquivo.write(('Data:{0} - {1:.2f} Tarifa:{2:.2f} Saldo: {3:.2f} \n'.format(dia.strftime('%Y-%m-%d %h %H:%M'), compra, tarifa, lista[-1][-1])))
                    # fechar o arquivo
                    arquivo.close()
                # condição em caso do user não poder realizar a compra
                else:
                    # mensagem para a condição 
                    print('Saldo não suficiente!')
                # mensagem que aparecerá na tela
            print('Débito feito com êxito!')
        # condição em caso de errar a senha
        elif lista[3][1] != senha:
            # mensagem da condição
            print('Senha incorreta, favor insirir uma senha válida!')
    # condição quando se erra o CPF
    else:
        # mensagem da condição
        print('Digita direito..')
    
# função para realizar o Deposito
def Deposita():
    # variavel para gravar o dia na compra 
    dia = datetime.now()
    # var para o user digitar o CPF
    cpf = input('Digite o CPF: ')
    # condição caso o CPF já exista
    if os.path.isfile(cpf+'.txt'):
        # var para o user digitar a senha
        senha = input('Digite a senha do usuário: ')
        # abrir o arquivo em modo de LEITURA
        arquivo = open(cpf+'.txt', 'r')
        # abrir uma lista
        lista = []
        # var para ler o arquivo
        leitor = arquivo.readlines()
        # fechar o arquivo
        arquivo.close()
        # for para organizar a leitura do arquivo
        for x in leitor:
            # var para tirar o \n da lista
            organiza = x.split()
            # guardar os dados, já organizados, em ordem dentro da lista
            lista.append(organiza)
        # condição para segurança do banco
        if lista[1][1] == cpf and lista [3][1] == senha:
            # var para o user colocar o valor a ser depositado
            deposita = float(input('Digite o valor a ser depositado: '))
            # realizar a conta para o novo saldo
            lista[-1][-1] = float(lista[-1][-1]) + deposita
            # abrir o arquivo em modo APPEND
            arquivo = open(cpf+'.txt', 'a')
            # escrever sempre a nova compra em baixo da anterior para criar uma espécie de histórico dos depósitos
            arquivo.write('Data:{0} + {1:.2f} Tarifa: 0.00 Saldo: {2:.2f} \n'.format(dia.strftime('%Y-%m-%d %h %H:%M'), deposita, lista[-1][-1]))
            # fechar o arquivo
            arquivo.close()
            # mensagem que aparecerá na tela
            print('Depósito feito com êxito!')
        # condição para se a senha estiver errada
        elif lista[3][1] != senha:
            # mensagem para a condição
            print('Senha incorreta, favor insirir uma senha válida!')
    # condição para se o CPF estiver errado
    else:
        # mensagem da condição
        print('Mai de novo sor?? Colobara aew')

# função para ver o saldo
def Saldo():
    # var para o user digitar o CPF
    cpf = input('Digite o CPF: ')
    # condição para achar o CPF
    if os.path.isfile(cpf+'.txt'):
        # var para o user digitar a senha
        senha = input('Digite a senha do usuário: ')
        # abrir o arquivo em modo LEITURA
        arquivo = open(cpf+'.txt', 'r')
        # abrir uma lista[]
        lista = []
        # var para ler o arquivo
        leitor = arquivo.readlines()
        # fechar o arquivo
        arquivo.close()
        # for para organizar a leitura do arquivo
        for x in leitor:
            # var para tirar o \n da lista
            organiza = x.split()
            # guardar os dados, já organizados, em ordem dentro da lista
            lista.append(organiza)
        # condição de segurança do banco
        if lista[1][1] == cpf and lista [3][1] == senha:
            # mostrar a Data e o saldo do cliente
            print(lista[-1][0], lista[-1][1], lista[-1][-2], lista[-1][-1])
        # condição em caso da senha estar incorreta
        elif lista[3][1] != senha:
            # mensagem para a condição
            print('Senha incorreta, favor insirir uma senha válida!')
    # condição em caso do fps estar incorreto
    else:
        # mensagem da condição
        print('Não quero mais falar com o senhor, você acha que eu estou errando ;-;')
# função para mostrar o Extrato da conta
def Extrato():
    # var para o user digitar o CPF
    cpf = input('Digite o CPF: ')
    # condição para caso o CPF já existir
    if os.path.isfile(cpf+'.txt'):
        # var para o user digitar a senha
        senha = input('Digite a senha do usuário: ')
        # abrir o arquivo em modo de LEITURA
        arquivo = open(cpf+'.txt', 'r')
        # criar uma lista[]
        lista = []
        # var para ler o arquivo
        leitor = arquivo.readlines()
        # fechar o arquivo
        arquivo.close()
        # for para organizar a leitura do arquivo
        for x in leitor:
            # var para tirar o \n da lista
            organiza = x.split()
            # guardar os dados, já organizados, em ordem dentro da lista
            lista.append(organiza)
        # condição de segurança do banco
        if lista[1][1] == cpf and lista [3][1] == senha:
            # mostra o Nome do user
            print('\nNome: %s' % lista[0][1])
            # mostra o CPF do user
            print('\nCPF: %s' % lista[1][1])
            # mostra o tipo da conta do user
            print('\nTipo da Conta: %s\n' % lista [2][1])
            # for para varrer a lista e mostrar todas as transações que foram feitas
            for x in range(4,len(lista)):
                # mostrando a lista de forma formatada
                print(*lista[x])
        # condição para caso da senha estar incorreta
        elif lista[3][1] != senha:
            # mensagem da condição
            print('Senha incorreta, favor insirir uma senha válida!')
    # condição para caso o CPF não exista
    else:
        # mensagem da condição
        print('A idade chega pra todos, né?? kkkkkkkk')

# função principal
def main():
    # crianção de um loop infinito
    while True:
        # pular linha
        print()
        # deixar a interface mais amigavel para o user
        print('------Menu------')
        # mesma coisa
        print()
        # apresentar todas as opções para o user
        print('1 - Novo Cliente')
        print('2 - Apaga Cliente')
        print('3 - Debita')
        print('4 - Deposita')
        print('5 - Saldo')
        print('6 - Extrato')
        print()
        print()
        print('0 - Sai')
        print()
        # var para o user escolher uma das opções das quais foram apresentadas
        opcao = input('Escolha uma das opções: ')

        # condições para executar cada função, de acordo com que o user digitar
        if opcao == '1':
            Novo()
        elif opcao == '2':
            Apaga()
        elif opcao == '3':
            Debita()
        elif opcao == '4':
            Deposita()
        elif opcao == '5':
            Saldo()
        elif opcao == '6':
            Extrato()
        elif opcao == '0':
            break
        # caso o user seja teimoso e digite errado, para sair do codigo
        else:
            break
# chamar a função principal para executar o código
main()