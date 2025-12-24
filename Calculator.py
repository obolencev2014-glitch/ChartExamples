import tkinter as tk

window = tk.Tk()
window.geometry("550x350")
window.title("Программа анализа csv файлов")


label_00 = tk.Label(text="Файл:")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text="")
label_01.grid(row=0, column=1, sticky="w")

label_10 = tk.Label(text="Строк:")
label_10.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_11 = tk.Label(text="")
label_11.grid(row=1, column=1, sticky="w")

label_20 = tk.Label(text="Столбцов:")
label_20.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_21 = tk.Label(text="")
label_21.grid(row=2, column=1, sticky="w")


from tkinter.scrolledtext import ScrolledText

output_text = ScrolledText(height=10, width=50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

button = tk.Button(
    window,
    text="Прочитать файл"
)
button.grid(row=4, column=1)

def process_button():
    output_text.delete(1.0, tk.END) 
    
    from tkinter import filedialog as fd

def do_dialog():
    return fd.askopenfilename()

# ---------- запуск ----------
window.mainloop()
