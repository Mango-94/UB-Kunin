import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Функция для простого калькулятора
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Деление на ноль"
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: Неверное значение")

# Функция выбора чекбоксов
def show_choice():
    choices = []
    if checkbox1_var.get():
        choices.append("Первый вариант")
    if checkbox2_var.get():
        choices.append("Второй вариант")
    if checkbox3_var.get():
        choices.append("Третий вариант")
    if choices:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(choices)}")
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

# Функция загрузки текста
def load_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, text_content)

# Главное окно
app = tk.Tk()
app.title("Кунин Михаил Александрович")
app.geometry("400x300")

# Вкладки
notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Первая вкладка: Калькулятор
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Калькулятор")

entry1 = ttk.Entry(frame1, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

operation_var = tk.StringVar(value="+")
operation_menu = ttk.Combobox(frame1, textvariable=operation_var, values=["+", "-", "*", "/"], width=5, state='readonly')
operation_menu.grid(row=0, column=1, padx=5, pady=5)

entry2 = ttk.Entry(frame1, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

calc_button = ttk.Button(frame1, text="Вычислить", command=calculate)
calc_button.grid(row=0, column=3, padx=5, pady=5)

result_label = ttk.Label(frame1, text="Результат: ")
result_label.grid(row=1, column=0, columnspan=4, pady=5)

# Вторая вкладка: Чекбоксы
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Чекбоксы")

checkbox1_var = tk.BooleanVar()
checkbox1 = ttk.Checkbutton(frame2, text="Первый", variable=checkbox1_var)
checkbox1.pack(anchor="w", padx=10, pady=5)

checkbox2_var = tk.BooleanVar()
checkbox2 = ttk.Checkbutton(frame2, text="Второй", variable=checkbox2_var)
checkbox2.pack(anchor="w", padx=10, pady=5)

checkbox3_var = tk.BooleanVar()
checkbox3 = ttk.Checkbutton(frame2, text="Третий", variable=checkbox3_var)
checkbox3.pack(anchor="w", padx=10, pady=5)

choose_button = ttk.Button(frame2, text="Показать выбор", command=show_choice)
choose_button.pack(pady=10)

# Третья вкладка: Работа с текстом
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Текст")

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text)

text_area = tk.Text(frame3, wrap="word")
text_area.pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()
