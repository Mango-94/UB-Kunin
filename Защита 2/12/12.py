import tkinter as tk
from tkinter import messagebox, filedialog
import requests

result = "" # Переменная для хранения результатов данных

# Получение данных о репозитории
def fetch_repo_data():
    repo_name = entry.get()
    if not repo_name:
        messagebox.showwarning("Ошибка", "Введите имя репозитория!")
        return

    url = f"https://api.github.com/repos/{repo_name}" # apache/spark
    try:
        response = requests.get(url)
        if response.status_code == 200:
            repo_data = response.json()
            global result
            result = (
                f"Компания: {repo_data.get('company', None)}\n"
                f"Создано: {repo_data['created_at']}\n"
                f"Email: {repo_data.get('email', None)}\n"
                f"ID: {repo_data['id']}\n"
                f"Имя: {repo_data['name']}\n"
                f"URL: {repo_data['owner']['url']}"
            )
        else:
            result = f"Ошибка {response.status_code}: {response.json().get('message', 'Неизвестная ошибка')}"
    except requests.RequestException as e:
        result = f"Ошибка при выполнении запроса: {e}"

    output_label.config(text=result)

# Запись данных в отдельный файл
def save_data_to_file():
    if not result:
        messagebox.showwarning("Ошибка", "Нет данных для сохранения!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"),
        ("All files", "*.*")], title="Сохранить как")
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(result)
            messagebox.showinfo("Окно", "Данные успешно сохранены")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

# GUI
root = tk.Tk()
root.title("Программа")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Введите имя репозитория:")
label.pack()

entry = tk.Entry(frame, width=40)
entry.pack()

fetch_button = tk.Button(frame, text="Получить данные", command=fetch_repo_data)
fetch_button.pack(pady=5)

save_button = tk.Button(frame, text="Сохранить данные в файл", command=save_data_to_file)
save_button.pack(pady=5)

output_label = tk.Label(frame, text="", justify="left", wraplength=400)
output_label.pack(pady=5)

root.mainloop()
