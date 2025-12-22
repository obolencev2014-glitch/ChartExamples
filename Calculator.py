
# Python калькулятор
# Программа умножает два введённых числа

import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Python Калькулятор")


# ----- Виджеты ввода -----
first_label = tk.Label(text="Введите первое число:")
first_label.grid(column=0, row=0, padx=10, pady=10)

first_entry = tk.Entry()
first_entry.grid(column=1, row=0)


second_label = tk.Label(text="Введите второе число:")
second_label.grid(column=0, row=1, padx=10, pady=10)

second_entry = tk.Entry()
second_entry.grid(column=1, row=1)


# ----- Виджет результата -----
result_label = tk.Label(text="Результат: ")
result_label.grid(column=0, row=2, sticky="w", padx=10, pady=10)


# ----- Функция умножения -----
def get_mul():
    """Читает числа из полей ввода и выводит произведение."""
    a = int(first_entry.get())
    b = int(second_entry.get())
    result_label['text'] = f"Результат: {a * b}"


# ----- Кнопка -----
button = tk.Button(window, text="Вычислить *", command=get_mul)
button.grid(column=1, row=2)


window.mainloop()
