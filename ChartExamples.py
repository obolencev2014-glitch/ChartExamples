import tkinter as tk

# импорт внешних файлов
import chart1
import chart2

# функция закрытия программы
def do_close():
    window.destroy()

# создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# заголовок
lblTitle = tk.Label(
    window,
    text="Примеры построения графиков",
    font=("Helvetica", 16, "bold"),
    fg="#0000cc"
)
lblTitle.place(x=55, y=25)

# кнопка + метка для графика 1
btnChart1 = tk.Button(
    window,
    text="График 1",
    font=("Helvetica", 10, "bold"),
    command=chart1.plot_chart
)
btnChart1.place(x=40, y=115, width=90, height=30)

lblChart1 = tk.Label(window, text="График синуса matplotlib")
lblChart1.place(x=170, y=122)

# кнопка + метка для графика 2
btnChart2 = tk.Button(
    window,
    text="График 2",
    font=("Helvetica", 10, "bold"),
    command=chart2.plot_chart
)
btnChart2.place(x=40, y=165, width=90, height=30)

lblChart2 = tk.Label(window, text="Нормальное распределение")
lblChart2.place(x=170, y=172)

# кнопка закрытия
btnClose = tk.Button(
    window,
    text="Закрыть",
    font=("Helvetica", 10, "bold"),
    command=do_close
)
btnClose.place(x=330, y=400, width=90, height=30)

# запуск цикла
window.mainloop()

