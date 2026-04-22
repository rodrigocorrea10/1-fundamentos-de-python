import tkinter as tk

janela = tk.Tk()
janela.title('Ler Entry')
janela.geometry('600x400')

frame1 = tk.Frame(janela, bg='lightgreen', width=560, height=150, bd=1)
frame1.place(x=20, y=30)

# frame2 = tk.Frame(janela, bg='ligthgreen', width=560, height=150, bd=2)
# frame2.place(x=100, y=20)

label1 = tk.Label(frame1, text='Digite seu email:', bg='lightgreen')
label1.place(x=25, y=8)

label2 = tk.Label(frame1, text='Digite sua senha:', bg='lightgreen')
label2.place(x=25, y=30)

janela_email = tk.Entry(janela, width=40)
janela_email.place(x=280, y=40)

janela_senha = tk.Entry(janela, width=40, show='*')
janela_senha.place(x=280, y=65)

button = tk.Button(janela, width=30, text='Submit', bg='green')
button.place(x=190, y=100)

janela.mainloop()
