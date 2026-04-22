import tkinter as tk

janela = tk.Tk()
janela.title('Estrutura Base')
janela.geometry('400x200')

frame1 = tk.Frame(janela, bg='lightblue', width=100, height=200, bd=1)
frame1.place(x=0, y=0)

frame2 = tk.Frame(janela, bg='lightgreen', width=300, height=150, bd=2)
frame2.place(x=100, y=0)

frame3 = tk.Frame(janela, bg='yellow', width=400, height=50, bd=3)
frame3.place(x=100, y=150)

label1 = tk.Label(frame1, text="Frame Esquerdo", bg='lightblue')
label1.place(x=0, y=0)

label2 = tk.Label(frame2, text="Frame Direito", bg='lightgreen')
label2.place(x=0, y=0)

label3 = tk.Label(frame3, text="Frame Inferior Direito", bg='yellow')
label3.place(x=0, y=0)

janela.mainloop()
