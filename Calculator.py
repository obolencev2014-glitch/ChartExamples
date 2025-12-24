# ==========================================
# Программа анализа CSV файлов (базовая)
# ==========================================

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
import pandas as pd
import os

# ---------- главное окно ----------
window = tk.Tk()
window.geometry("550x350")
window.title("Программа анализа csv файлов")

# ---------- поля вывода ----------
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

# ---------- текстовый вывод ----------
output_text = ScrolledText(height=10, width=50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# ---------- диалог выбора файла ----------
def do_dialog():
    my_dir = os.getcwd()
    return fd.askopenfilename(initialdir=my_dir)

# ---------- чтение CSV ----------
def pandas_read_csv(file_name):
    df = pd.read_csv(file_name, header=None)
    label_11["text"] = df.shape[0]
    label_21["text"] = df.shape[1]
    return df

# ---------- выбор столбца ----------
def get_column(df, col_idx):
    lst = []
    for i in range(df.shape[0]):
        lst.append(str(df.iat[i, col_idx]))
    return lst

# ---------- обработка кнопки ----------
def process_button():
    output_text.delete(1.0, tk.END)

    file_name = do_dialog()
    if not file_name:
        return

    label_01["text"] = file_name

    df = pandas_read_csv(file_name)

    for col in range(df.shape[1]):
        values = get_column(df, col)
        output_text.insert(
            tk.END,
            f"Столбец №{col}: {len(values)} значений\n"
        )

# ---------- кнопка ----------
button = tk.Button(
    window,
    text="Прочитать файл",
    command=process_button
)
button.grid(row=4, column=1)

# ---------- запуск ----------
window.mainloop()
