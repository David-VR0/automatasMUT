import tkinter as tk

def ventana2(lista, control):
    root = tk.Tk()  # creamos la ventana
    root.title("CINTA")
    root.resizable(0, 0)
    root.geometry("800x100+300+400")

    objeto=iter(lista)
    label = tk.Label(root, text=next(objeto), font=("italic", 20), width=(50), height=(15), fg="blue")

    label.pack()

    def refresh():
        try:
            label['text'] = next(objeto)
            root.after(100, refresh)
        except StopIteration:
            root.after(100000, root.destroy)
    if control == True:
        root.after(100, refresh)
        root.mainloop()