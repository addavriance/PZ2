import tkinter as tk
from tkinter import ttk

import PZ_5 as PZ


def task_5(tab_control, history_text):
    def calculate_steps():
        num = int(entry_num.get())
        steps = PZ.find_steps_to_zero(num)
        result = f"Количество шагов до нуля числа {num}: {steps}"
        result_label.config(text=result)
        update_history("[5] " + result, history_text)

    tab_5 = ttk.Frame(tab_control)
    tab_control.add(tab_5, text='5')

    label_num = ttk.Label(tab_5, text="Введите число:")
    label_num.pack(pady=5)

    entry_num = ttk.Entry(tab_5)
    entry_num.pack(pady=5)

    calculate_button = ttk.Button(tab_5, text="Вычислить", command=calculate_steps)
    calculate_button.pack(pady=5)

    result_label = ttk.Label(tab_5, text="")
    result_label.pack(pady=5)


def task_5_1(tab_control, history_text):
    def perform_shift():
        A1 = float(A1_entry.get())
        B1 = float(B1_entry.get())
        C1 = float(C1_entry.get())
        A2 = float(A2_entry.get())
        B2 = float(B2_entry.get())
        C2 = float(C2_entry.get())

        A1, B1, C1 = PZ.ShiftLeft3(A1, B1, C1)
        A2, B2, C2 = PZ.ShiftLeft3(A2, B2, C2)

        result_1 = f"Числа 1 после сдвига: {A1}, {B1}, {C1}"
        result_2 = f"Числа 2 после сдвига: {A2}, {B2}, {C2}"

        result_label_1.config(text=result_1)
        result_label_2.config(text=result_2)

        update_history(f"""[5.1] {result_1}\n      {result_2}""", history_text)

    tab_5_1 = ttk.Frame(tab_control)
    tab_control.add(tab_5_1, text='5.1')

    label_set_1 = ttk.Label(tab_5_1, text="Введите числа для списка 1:")
    label_set_1.pack(pady=5)

    A1_entry = ttk.Entry(tab_5_1)
    A1_entry.pack(pady=5)

    B1_entry = ttk.Entry(tab_5_1)
    B1_entry.pack(pady=5)

    C1_entry = ttk.Entry(tab_5_1)
    C1_entry.pack(pady=5)

    label_set_2 = ttk.Label(tab_5_1, text="Введите числа для списка 2:")
    label_set_2.pack(pady=5)

    A2_entry = ttk.Entry(tab_5_1)
    A2_entry.pack(pady=5)

    B2_entry = ttk.Entry(tab_5_1)
    B2_entry.pack(pady=5)

    C2_entry = ttk.Entry(tab_5_1)
    C2_entry.pack(pady=5)

    perform_button = ttk.Button(tab_5_1, text="Сдвиг", command=perform_shift)
    perform_button.pack(pady=5)

    result_label_1 = ttk.Label(tab_5_1, text="")
    result_label_1.pack(pady=5)

    result_label_2 = ttk.Label(tab_5_1, text="")
    result_label_2.pack(pady=5)


def update_history(result, history_text):
    history_text.config(state=tk.NORMAL)
    history_text.insert(tk.END, result + "\n")
    history_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    root.title("Задания")

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    history_label = ttk.Label(root, text="История:")
    history_label.pack(pady=5)

    history_frame = ttk.Frame(root)
    history_frame.pack(pady=5, fill='both', expand=True)

    history_text = tk.Text(history_frame, height=10, state=tk.DISABLED, wrap='word')
    history_text.pack(side='left', fill='both', expand=True)

    history_scrollbar = ttk.Scrollbar(history_frame, orient='vertical', command=history_text.yview)
    history_scrollbar.pack(side='right', fill='y')

    history_text.config(yscrollcommand=history_scrollbar.set)

    task_5(tab_control, history_text)
    task_5_1(tab_control, history_text)

    root.mainloop()


if __name__ == "__main__":
    main()
