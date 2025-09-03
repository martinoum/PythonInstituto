from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio 12")
ventana.geometry("600x600")
ventana.config(bg="#76a87b")

miFrame = Frame()
miFrame.pack(fill="both",expand="yes")
miFrame.config(bg="#76a87b",cursor="heart",relief="groove")
miFrame.place(x=300,y=300,anchor="center")

nombre = Label(miFrame,text="Martino Uvilla",fg="white",bg="#76a87b",font=("Impact",24,"bold"))
nombre.pack()
subtitulo = Label(miFrame,text="Primer año - 2025 ",fg="white",background="#76a87b",font=("Impact",18,"bold"))
subtitulo.pack()
subtitulo2 = Label(miFrame, text="Instituto Nuevo Cuyo",fg="white",bg="#76a87b",font=("Impact",18,"bold"))
subtitulo2.pack()

btn_mensaje = Button(miFrame, text="Click",bg="#111111",fg="white",command= lambda: messagebox.showinfo("Mensaje","turf - pasos al costado"))
btn_mensaje.pack()


ventana.mainloop()