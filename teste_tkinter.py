import tkinter as tk 

janela = tk.Tk()
janela.geometry('600x600')
#.pack() empilhamento automático (vertical ou horizontal). Ideal para layouts simples
#.grid() Estrutura em grade (linhas e colunas). Perfeito para formulários e alinhamento preciso. 
#.place() Posicionamento 
button = tk.Button(janela, text='Entrar', bg='lightblue', command='')
button.pack()

janela.mainloop()