import tkinter as tk
from tkinter import filedialog
import subprocess

def ejecutar_bat():
    ubicacion_carpeta = ubicacion_var.get()
    nombre_archivo = nombre_archivo_var.get()
    
    if ubicacion_carpeta and nombre_archivo:
        comando = f'@echo off\ncd /d {ubicacion_carpeta}\npyinstaller --onefile --noconsole {nombre_archivo}'
        with open('temp.bat', 'w') as archivo_bat:
            archivo_bat.write(comando)
        subprocess.Popen('temp.bat', shell=True)
        etiqueta_estado.config(text="Cargando...")
    else:
        etiqueta_estado.config(text="Error: Debes seleccionar un archivo .py antes de ejecutar.")

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Python", "*.py")])
    if archivo:
        ubicacion = "/".join(archivo.split("/")[:-1])
        nombre_archivo = archivo.split("/")[-1]
        ubicacion_var.set(ubicacion)
        nombre_archivo_var.set(nombre_archivo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejecutar PyInstaller")
ventana.geometry("400x220")

# Variables para almacenar la ubicación de la carpeta y el nombre del archivo .py
ubicacion_var = tk.StringVar()
nombre_archivo_var = tk.StringVar()

# Etiqueta y entrada para la ubicación de la carpeta
etiqueta_ubicacion = tk.Label(ventana, text="Ubicación de la carpeta:")
etiqueta_ubicacion.pack()
entrada_ubicacion = tk.Entry(ventana, textvariable=ubicacion_var)
entrada_ubicacion.pack()

# Etiqueta y entrada para el nombre del archivo
etiqueta_nombre_archivo = tk.Label(ventana, text="Nombre del archivo:")
etiqueta_nombre_archivo.pack()
entrada_nombre_archivo = tk.Entry(ventana, textvariable=nombre_archivo_var)
entrada_nombre_archivo.pack()

# Botón para seleccionar archivo .py
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo .py", command=seleccionar_archivo)
boton_seleccionar.pack()

# Botón para ejecutar el archivo .bat
boton_ejecutar = tk.Button(ventana, text="Ejecutar .bat", command=ejecutar_bat)
boton_ejecutar.pack()

# Etiqueta para mostrar el estado de la ejecución
etiqueta_estado = tk.Label(ventana, text="")
etiqueta_estado.pack()

ventana.mainloop()
