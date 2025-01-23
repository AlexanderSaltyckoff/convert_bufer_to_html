import os
import pyperclip
import subprocess

# Получение текста из буфера обмена
clipboard_content = pyperclip.paste()

# Определение пути до рабочего стола
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_name = "clipboard_content.html"
file_path = os.path.join(desktop_path, file_name)

# Запись содержимого буфера обмена в файл .html
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(clipboard_content)

print(f"Файл '{file_name}' успешно создан на рабочем столе.")

# Открытие файла
subprocess.Popen(['start', file_path], shell=True)