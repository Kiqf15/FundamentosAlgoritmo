from tkinter import *
from tkinter import scrolledtext    

window = Tk()
window.title("Projeto de Python")
window.geometry("900x600")

palavra = Label(window, text="Palavra Suspeita: ", font=("Arial", 14))
palavra.place(relx=0.05, rely=0.08)

quantidade = Label(window, text="Frequencia: ", font=("Arial", 14))
quantidade.place(relx=0.05, rely=0.15)

txt = scrolledtext.ScrolledText(window, width=100, height=23)
txt.place(relx=0.05, rely=0.35)

palavraEntrada = Entry(window, width=15, font=("Arial", 14))
palavraEntrada.place(relx=0.25, rely= 0.08)

frequencia = Entry(window, width=15, font=("Arial", 14))
frequencia.place(relx=0.25, rely=0.15)

def buscaPalavras():
  pass


pesquisar = Button(window, text="Pesquisar", command=buscaPalavras)
pesquisar.place(relx=0.5, rely=0.08)

quantidade = Label(window, text="Ocorrências: ", font=("Arial", 14))
quantidade.place(relx=0.05, rely=0.3)

txt.inset(END, "Este é um trecho do chat")

window.mainloop()