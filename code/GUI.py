import tkinter as tk
from tkinter import ttk
import qrcode
from create_qr_code import create_qr_code
from PIL import ImageColor

error_correction_options = {
    "L: correct 7% of errors": "L",
    "M: correct 15% of errors": "M",
    "Q: correct 25% of errors": "Q",
    "H: correct 30% of errors": "H"
    }

def generate_qr():
    url = url_entry.get()
    version = int(version_entry.get())
    fill_color = fill_color_entry.get()
    back_color = back_color_entry.get()
    box_size = int(box_size_entry.get())
    error_correction = error_correction_var.get()
    error_code = error_correction_options[error_correction]
    filename = filename_entry.get() + '.png'
    
    create_qr_code(url, fill=fill_color, back=back_color, version=version, box_size=box_size, error_correction=error_code, filename=filename)

root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Version (put 1 - 40):").pack()
version_entry = tk.Entry(root, width=5)
version_entry.pack()

tk.Label(root, text="Fill Color (e.g., 'red' or 'rgb(255,0,0)'):").pack()
fill_color_entry = tk.Entry(root, width=15)
fill_color_entry.pack()

tk.Label(root, text="Background Color (e.g., 'red' or 'rgb(255,0,0)'):").pack()
back_color_entry = tk.Entry(root, width=15)
back_color_entry.pack()

tk.Label(root, text="Box Size:").pack()
box_size_entry = tk.Entry(root, width=5)
box_size_entry.pack()

tk.Label(root, text="Error Correction:").pack()
error_correction_var = tk.StringVar()
error_correction_dropdown = ttk.Combobox(root, textvariable=error_correction_var, values=list(error_correction_options.keys()))
error_correction_dropdown.pack()

tk.Label(root, text="Filename(withou .png):").pack()
filename_entry = tk.Entry(root, width=20)
filename_entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

root.mainloop()
