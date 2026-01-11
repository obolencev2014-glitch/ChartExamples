import tkinter as tk

def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Пример построения графиков")

# Кнопка закрытия
btn_close = tk.Button(
    window,
    text="Закрыть",
    font=("Helvetica", 10, "bold"),
    command=do_close
)
btn_close.place(x=180, y=200, width=90, height=30)

window.mainloop()

