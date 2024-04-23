from tkinter import *
from tkinter import messagebox
from datetime import datetime
from random import randrange
import os

janela = Tk()
janela.title("Cadastro")
janela.geometry("800x800")

def cadastrar():
    cpf2 = cpf1.get()
    nome2 = nome1.get()
    data2 = data1.get().replace("-","/").split("/")
    ende2 = ende1.get()
    prof2 = prof1.get()
    if os.path.isfile("./teste/"+cpf2+".txt"):
        messagebox.showinfo("Aviso","CPF já cadastrado")
    else:
        arquivo = open("./teste/"+cpf2+".txt", "w")
        ano = datetime.now().year
        anoX = int(data2[-1])
        idade = ano - anoX
        ID = []
        for i in range(5):
            ID.append(str(randrange(9)))
        arquivo.write(f"ID: {''.join(ID)}\nCPF: {cpf2}\nNome: {nome2}\nData de nascimento: {'/'.join(data2)}  Idade: {idade}\nEndereço: {ende2}\nProfissão: {prof2}")
        arquivo.close()
        messagebox.showinfo("Cadastro", "Cadastro efetuado com sucesso")


Label(janela, text="CPF:", font=20).place(relx=0.1,rely=0.1)
cpf1 = Entry(janela)
cpf1.place(relx=0.3, rely=0.1)

Label(janela, text="Nome:", font=20).place(relx=0.1,rely=0.2)
nome1 = Entry(janela)
nome1.place(relx=0.3, rely=0.2)

Label(janela, text="Data de Nascimento:\n{dd/mm/aaaa}", font=20).place(relx=0.1,rely=0.3)
data1 = Entry(janela)
data1.place(relx=0.3, rely=0.3)

Label(janela, text="Endereço:", font=20).place(relx=0.1,rely=0.4)
ende1 = Entry(janela)
ende1.place(relx=0.3, rely=0.4)

Label(janela, text="Profissão:", font=20).place(relx=0.1,rely=0.5)
prof1 = Entry(janela)
prof1.place(relx=0.3, rely=0.5)

botao = Button(janela, text="Cadastrar", command=cadastrar)
botao.place(relx=0.1, rely=0.6, width=100)

janela.mainloop()