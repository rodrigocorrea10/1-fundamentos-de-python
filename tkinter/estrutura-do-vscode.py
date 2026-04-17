import tkinter as tk

janela = tk.Tk()
janela.title('Estrutura do VS Code')
janela.geometry('400x200')

frame1 = tk.Frame(janela, bg='lightblue', width=100, height=200, bd=1)
frame1.place(x=0, y=0)

frame2 = tk.Frame(janela, bg='green', width=400, height=30, bd=2)
frame2.place(x=100, y=0)

frame3 = tk.Frame(janela, bg='lightgreen', width=400, height=130, bd=3)
frame3.place(x=100, y=30)

frame4 = tk.Frame(janela, bg='yellow', width=400, height=50, bd=4)
frame4.place(x=100, y=150)

label1 = tk.Label(frame1, text='Explorador', bg='lightblue')
label1.place(x=5, y=10)

label2 = tk.Label(frame2, text='Página do código', bg='green')
label2.place(x=25, y=0)

label3 = tk.Label(frame3, text='Editor do código', bg='lightgreen')
label3.place(x=25, y=10)

label4 = tk.Label(frame4, text='Terminal', bg='yellow')
label4.place(x=25, y=5)

janela.mainloop()
