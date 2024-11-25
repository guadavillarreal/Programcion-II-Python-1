import tkinter as tk

# Crear la ventana principal con dimensiones y color de fondo
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("600x500")
ventana.configure(bg="#EEDD82")  # Color de fondo almendra

# Crear un marco para contener el texto y el párrafo
marco_izquierdo = tk.Frame(ventana, bg="#EEDD82")  # Mismo color que la ventana
marco_izquierdo.pack(side="left", fill="both", expand=True)

# Crear una etiqueta para el título
titulo = tk.Label(marco_izquierdo, text="Este es el título", font=("Helvetica", 16), bg="black")
titulo.pack(pady=100)

# Crear una etiqueta para el párrafo
parrafo = tk.Label(marco_izquierdo, text="Este es un párrafo de ejemplo. Puedes agregar más texto aquí.", bg="black")
parrafo.pack()

# Crear un marco para contener los botones
marco_derecho = tk.Frame(ventana, bg="#e0d8b0", width=700, height=700, )  # Color pistacho y dimensiones fijas
marco_derecho.pack(side="right")

# Crear los botones
boton_registrarse = tk.Button(marco_derecho, text="Registrarse")
boton_ingresar = tk.Button(marco_derecho, text="Ingresar")

# Centrar los botones verticalmente en el marco derecho
boton_registrarse.pack(pady=25)
boton_ingresar.pack(pady=25)

# Ejecutar la aplicación
ventana.mainloop()