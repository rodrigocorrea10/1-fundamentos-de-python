import tkinter as tk

janela = tk.Tk()
janela.geometry('600x600')

scrollbar = tk.Scrollbar(janela)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

janela_email = tk.Entry(janela, width=40) #width = Largura, Height = Altura
janela_email.pack(pady=10)

janela_senha = tk.Entry(janela, show='*')
janela_senha.pack(pady=10)

verificar = tk.Checkbutton(janela, text='Exibir a sennha')
verificar.pack(pady=10)

button = tk.Button(janela, text='Entrar', bg='lightblue', command='')
button.pack(pady=10)

button = tk.Button(janela, text='Fechar', bg='red', command= janela.destroy)
button.pack(pady=50)

janela.mainloop()