#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrcode

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

# Ejemplo de uso
url = "https://www.ejemplo.com"  # URL que deseas codificar en el QR
file_name = "codigo_qr.png"  # Nombre del archivo de imagen del código QR

generate_qr_code(url, file_name)


# In[3]:


import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import os

def generate_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "codigo_qr.png"
    img.save(img_path)

    # Cargar la imagen generada utilizando PIL
    img_pil = Image.open(img_path)

    # Redimensionar la imagen para ajustar el campo de imagen
    img_pil = img_pil.resize((300, 300), Image.ANTIALIAS)

    # Crear objeto PhotoImage desde la imagen PIL
    qr_image.img_tk = ImageTk.PhotoImage(img_pil)

    # Actualizar el campo de imagen
    qr_image.configure(image=qr_image.img_tk)

def clear_image():
    # Borrar el archivo de imagen
    img_path = "codigo_qr.png"
    if os.path.exists(img_path):
        os.remove(img_path)

    # Borrar la imagen del campo de imagen
    qr_image.configure(image=None)

# Crear ventana principal
window = tk.Tk()
window.title("Generador de Código QR")

# Crear etiqueta y campo de entrada para la URL
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Crear botón para generar el código QR
generate_button = tk.Button(window, text="Generar QR", command=generate_qr_code)
generate_button.pack()

# Crear campo de imagen para mostrar el código QR generado
qr_image = tk.Label(window)
qr_image.pack()

# Crear botón para borrar la imagen
clear_button = tk.Button(window, text="Borrar Imagen", command=clear_image)
clear_button.pack()

# Iniciar bucle de la interfaz gráfica
window.mainloop()

