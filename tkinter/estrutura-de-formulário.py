import tkinter as tk

janela = tk.Tk()
janela.title('Estrutura de Formulário')
janela.geometry('600x400')

frame1 = tk.Frame(janela, bg='lightblue', width=560, height=50, bd=1)
frame1.place(x=20, y=10)

frame2 = tk.Frame(janela, bg='lightgreen', width=560, height=260, bd=2)
frame2.place(x=20, y=70)

frame3 = tk.Frame(janela, bg='yellow', width=560, height=50, bd=3)
frame3.place(x=20, y=340)

label1 = tk.Label(frame1, text='Frame Superior', bg='lightblue')
label1.place(x=250, y=13)

label2 = tk.Label(frame2, text='Frame do meio', bg='lightgreen')
label2.place(x=250, y=100)

label3 = tk.Label(frame3, text='Frase Inferior', bg='yellow')
label3.place(x=250, y=10)

janela.mainloop()
