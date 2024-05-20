import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk

HEADER_COLOR = "#04ADEF"
BASE_COLOR = "#717474"
BG_COLOR = "#f0f8ff"

root = tk.Tk()
root.title("PZ_17")
root.geometry("600x600")  # Увеличили высоту для размещения нового поля
root.configure(bg=BG_COLOR)

header_frame = tk.Frame(root, bg=HEADER_COLOR)
header_label = tk.Label(header_frame, text="Создание нового сайта", font=("Helvetica", 18), bg=HEADER_COLOR, fg="white")
header_label.pack(pady=10)
header_frame.pack(fill=tk.X)

content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Настройка колонок для центрации элементов
for i in range(6):
    content_frame.grid_columnconfigure(i, weight=1)

def add_label_entry(frame, text, row):
    label = tk.Label(frame, text=text, bg=BG_COLOR, fg=HEADER_COLOR, font=("Helvetica", 14, "bold"), pady=10)
    label.grid(row=row, column=1, sticky="e")
    entry = tk.Entry(frame, width=30, highlightthickness=0, borderwidth=1, bg=BG_COLOR)
    entry.grid(row=row, column=2, columnspan=3, sticky="w")
    return entry

email_entry = add_label_entry(content_frame, "Email:", 0)
password_entry = add_label_entry(content_frame, "Пароль:", 1)
first_name_entry = add_label_entry(content_frame, "Имя:", 2)
last_name_entry = add_label_entry(content_frame, "Фамилия:", 3)
nickname_entry = add_label_entry(content_frame, "Никнейм:", 4)

# Date of Birth Section
dob_frame = tk.Frame(content_frame, bg=BG_COLOR)
dob_frame.grid(row=5, column=0, columnspan=6, sticky="ew", pady=10)
dob_frame.grid_columnconfigure(0, weight=1)
dob_frame.grid_columnconfigure(1, weight=0)
dob_frame.grid_columnconfigure(2, weight=0)
dob_frame.grid_columnconfigure(3, weight=0)
dob_frame.grid_columnconfigure(4, weight=0)
dob_frame.grid_columnconfigure(5, weight=1)

dob_label = tk.Label(dob_frame, text="Дата рождения:", bg=BG_COLOR, fg=HEADER_COLOR, font=("Helvetica", 14, "bold"))
dob_label.grid(row=0, column=1, sticky="e")

days = list(range(1, 32))
months = list(range(1, 13))
current_year = datetime.now().year
years = list(range(1913, current_year + 1))

day_combobox = ttk.Combobox(dob_frame, values=days, width=3, state="readonly")
day_combobox.grid(row=0, column=2, padx=(5, 5))
day_combobox.set(days[0])

month_combobox = ttk.Combobox(dob_frame, values=months, width=3, state="readonly")
month_combobox.grid(row=0, column=3, padx=(5, 5))
month_combobox.set(months[0])

year_combobox = ttk.Combobox(dob_frame, values=years, width=5, state="readonly")
year_combobox.grid(row=0, column=4, padx=(5, 5))
year_combobox.set(years[0])

# Gender Section
gender_frame = tk.Frame(content_frame, bg=BG_COLOR)
gender_frame.grid(row=6, column=0, columnspan=6, sticky="ew", pady=10)
gender_frame.grid_columnconfigure(0, weight=1)
gender_frame.grid_columnconfigure(1, weight=0)
gender_frame.grid_columnconfigure(2, weight=0)
gender_frame.grid_columnconfigure(3, weight=0)
gender_frame.grid_columnconfigure(4, weight=1)

gender_label = tk.Label(gender_frame, text="Пол:", bg=BG_COLOR, fg=HEADER_COLOR, font=("Helvetica", 14, "bold"))
gender_label.grid(row=0, column=1, sticky="e")

gender_var = tk.IntVar()
male_radio = tk.Radiobutton(gender_frame, text="Мужчина", variable=gender_var, value=1, bg=BG_COLOR, fg=BASE_COLOR, font=("Helvetica", 14))
male_radio.grid(row=0, column=2, padx=(5, 5))

female_radio = tk.Radiobutton(gender_frame, text="Женщина", variable=gender_var, value=2, bg=BG_COLOR, fg=BASE_COLOR, font=("Helvetica", 14))
female_radio.grid(row=0, column=3, padx=(5, 5))

# Residence Section
residence_label = tk.Label(content_frame, text="Место проживания:", bg=BG_COLOR, fg=HEADER_COLOR, font=("Helvetica", 14, "bold"), pady=10)
residence_label.grid(row=7, column=1, sticky="e")

cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород", "Челябинск", "Самара", "Ростов-на-Дону", "Уфа", "Другой город..."]
residence_combobox = ttk.Combobox(content_frame, values=cities, width=25, state="readonly")
residence_combobox.grid(row=7, column=2, columnspan=3, sticky="w")
residence_combobox.set(cities[-1])

# Security Code Section
security_frame = tk.Frame(content_frame, bg=BG_COLOR)
security_frame.grid(row=8, column=0, columnspan=6, sticky="ew", pady=10)
security_frame.grid_columnconfigure(0, weight=1)
security_frame.grid_columnconfigure(1, weight=0)
security_frame.grid_columnconfigure(2, weight=0)
security_frame.grid_columnconfigure(3, weight=0)
security_frame.grid_columnconfigure(4, weight=0)
security_frame.grid_columnconfigure(5, weight=1)

security_code_label = tk.Label(security_frame, text="Код безопасности:", bg=BG_COLOR, fg=HEADER_COLOR, font=("Helvetica", 14, "bold"))
security_code_label.grid(row=0, column=1, sticky="e")

security_code_entry = tk.Entry(security_frame, width=10, highlightthickness=0, borderwidth=1, bg=BG_COLOR)
security_code_entry.grid(row=0, column=2, padx=(5, 5))

arrow_image = Image.open("../assets/arrow_left.png")
arrow_image = arrow_image.resize((20, 20), Image.LANCZOS)
arrow_photo = ImageTk.PhotoImage(arrow_image)
arrow_label = tk.Label(security_frame, image=arrow_photo, bg=BG_COLOR)
arrow_label.grid(row=0, column=3)

security_code_image = Image.open("../assets/security_code.png")
security_code_image = security_code_image.resize((120, 40), Image.LANCZOS)
security_code_photo = ImageTk.PhotoImage(security_code_image)
security_code_image_label = tk.Label(security_frame, image=security_code_photo, bg=BG_COLOR)
security_code_image_label.grid(row=0, column=4, padx=(5, 5))

root.mainloop()
