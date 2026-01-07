# Программа анализа CSV файлов 
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import pandas as pd
import re


# ---------- функции-критерии ----------
def is_email(value):
    if pd.isna(value):
        return False
    return "@" in str(value)


def is_phone(value):
    if pd.isna(value):
        return False
    return bool(re.fullmatch(r"[+\d\s\-()]+", str(value)))


def is_number(value):
    try:
        float(value)
        return True
    except:
        return False


# ---------- анализ столбца ----------
def detect_column_type(series):
    total = len(series)
    email_cnt = 0
    phone_cnt = 0
    number_cnt = 0

    for v in series:
        if is_email(v):
            email_cnt += 1
        if is_phone(v):
            phone_cnt += 1
        if is_number(v):
            number_cnt += 1

    if email_cnt / total > 0.6:
        return "email"
    if phone_cnt / total > 0.6:
        return "телефон"
    if number_cnt / total > 0.6:
        return "числовой"
    return "текстовый"


# ---------- обработка кнопки ----------

def process_button():
    file_name = filedialog.askopenfilename(
        title="Выберите CSV файл",
        filetypes=[("CSV files", "*.csv")]
    )

    if not file_name:
        return

    # чтение CSV с учетом кодировки и разделителя
    try:
        df = pd.read_csv(
            file_name,
            sep=";",
            encoding="utf-8"
        )
    except:
        df = pd.read_csv(
            file_name,
            sep=";",
            encoding="cp1251"
        )

    output_text.delete(1.0, tk.END)

    output_text.insert(tk.END, f"Файл: {file_name}\n")
    output_text.insert(tk.END, f"Строк: {df.shape[0]}\n")
    output_text.insert(tk.END, f"Столбцов: {df.shape[1]}\n\n")
    output_text.insert(tk.END, "Определение типов столбцов:\n")

    for col in df.columns:
        col_type = detect_column_type(df[col])
        output_text.insert(tk.END, f"- {col}: {col_type}\n")


# ---------- интерфейс ----------
window = tk.Tk()
window.title("Анализ CSV файлов")
window.geometry("650x450")

label = tk.Label(window, text="Программа анализа CSV файлов", font=("Arial", 12))
label.pack(pady=10)

button = tk.Button(window, text="Открыть CSV файл", command=process_button)
button.pack(pady=5)

output_text = ScrolledText(window, width=80, height=20)
output_text.pack(padx=10, pady=10)

window.mainloop()

