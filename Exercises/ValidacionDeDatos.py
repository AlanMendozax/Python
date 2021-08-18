import re
import tkinter as tk
from tkinter import ttk, messagebox

#Metodo para validar.
def validar():

        # Validación del nombre de usuario.
        nombre = entry.get()
        if entry.get() == "":
            messagebox.showerror(message="Ingrese un nombre de usuario", title="Error de nombre")
        else:
            if re.match('^[(a-z,ñ,á,é,í,ó,ú0-9)]{10,15}$', nombre.lower()):
                messagebox.showinfo(message="El nombre es valido", title="Validación de nombre")
            else:
                messagebox.showerror(message="El nombre no es valido", title="Error de nombre")

        # Validación de la contraseña.
        contraseña = entry1.get()
        if entry1.get() == "":
            messagebox.showerror(message="Ingrese contraseña", title="Error de contraseña")
        else:
            if len(contraseña) < 8:
                messagebox.showerror(message="La contraseña no es valida, es menor de 8 caracteres", title="Error de contraseña")
            elif len(contraseña) == 15:
                messagebox.showerror(message="La contraseña no es valida, es mayor de 15 caracteres", title="Error de contraseña")
            elif re.search('[0-9]', contraseña) is None:
                messagebox.showerror(message="La contraseña no es valida, asegurate de que tenga al menos un número", title="Error de contraseña")
            elif re.search('[A-Z]', contraseña) is None:
                messagebox.showerror(message="La contraseña no es valida, asegurate de que tenga al menos una letra mayuscula", title="Error de contraseña")
            else:
                messagebox.showinfo(message="La contraseña es valida", title="Validación de contraseña")

        #validación de la confirmación de contraseña.
        if entry2.get() == "":
            messagebox.showerror(message="Repita la contraseña", title="Error de contraseña")

        # Validación del email.
        correo = entry3.get()
        if entry3.get() == "":
            messagebox.showerror(message="Ingrese un email", title="Error de email")
        else:
            if re.match('^[(a-z,ñ0-9\_\-\.)]+@[(a-z)]+\.[(a-z)]{2,15}$', correo.lower()):
                messagebox.showinfo(message="El correo es valido", title="Validación email")
            else:
                messagebox.showerror(message="El correo no es valido", title="Error email")

        # Validación de sexo.
        sexo = var.get()
        if sexo == 0:
            messagebox.showerror(message="Seleccione un genero", title="Error de genero")

        # Validación de fecha.
        fecha = entry4.get()
        if entry4.get() == "":
            messagebox.showerror(message="Ingrese una fecha", title="Error de fecha")
        else:
            if re.match('^[(1-35)]+-[(Enero),(Febrero),(Marzo),(Abril),(Mayo),(Junio),(Julio),(Agosto),(Septiembre),(Octubre),(Diciembre)]+-[0-9]{2,15}$', fecha.lower()):
                messagebox.showinfo(message="La fecha es valida", title="Validación de fecha")
            else:
                messagebox.showerror(message="La fecha no es valida", title="Error de fecha")

#Metodo para confirmar contraseñas
def confirmar(event):
    if entry2.get() == entry1.get():
        messagebox.showinfo(message="Las contraseñas coinciden", title="Validación de contraseña")
    else:
        messagebox.showerror(message="Las contraseñas no coinciden", title="Error de contraseña")

# Se crea el formulario.
root = tk.Tk()
root.config(width=280, height=250)
root.title("Form de registro")

# Crear componentes.
label = ttk.Label(root, text="Nombre de usuario: ").place(x=5, y=20)
label1 = ttk.Label(root, text="Contraseña: ").place(x=5, y=50)
label2 = ttk.Label(root, text="Confirmar contraseña: ").place(x=5, y=80)
label3 = ttk.Label(root, text="Email: ").place(x=5, y=110)
label4 = ttk.Label(root, text="Sexo: ").place(x=5, y=140)
label5 = ttk.Label(root, text="Fecha de nacimiento: ").place(x=5, y=170)
entry = ttk.Entry(root)
entry.place(x=130, y=20)
entry1 = ttk.Entry(root, show="*")
entry1.place(x=130, y=50)
entry2 = ttk.Entry(root, show="*")
entry2.place(x=130, y=80)
entry3 = ttk.Entry(root)
entry3.place(x=130, y=110)
var = tk.IntVar()
rb = ttk.Radiobutton(root, text="Hombre", variable=var, value=1).place(x=130, y=140)
rb1 = ttk.Radiobutton(root, text="Mujer", variable=var, value=2).place(x=210, y=140)
entry4 = ttk.Entry(root)
entry4.place(x=130, y=170)
entry2.bind('<FocusOut>', confirmar)
btn = ttk.Button(root, text="Validar", command=lambda: validar()).place(x=100, y=210)
root.mainloop()




