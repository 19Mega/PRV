import tkinter as tk

funcionalidad_actual = 1

def cambiar_funcionalidad():
    global funcionalidad_actual
    funcionalidad_actual = 2 if funcionalidad_actual == 1 else 1
    boton.config(text=f"Funcionalidad {funcionalidad_actual}")

def ejecutar_funcionalidad(event):
    if funcionalidad_actual == 1:
        lienzo.create_text(event.x, event.y, text="1", fill="white")
    else:
        lienzo.create_text(event.x, event.y, text="2", fill="black")

ventana = tk.Tk()

boton = tk.Button(ventana, text="Funcionalidad 1", command=cambiar_funcionalidad)
boton.pack()

lienzo = tk.Canvas(ventana, width=400, height=400, bg="gray")
lienzo.pack()

lienzo.bind("<Button-1>", ejecutar_funcionalidad)

ventana.mainloop()
