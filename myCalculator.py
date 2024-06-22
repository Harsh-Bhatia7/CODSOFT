import tkinter as tk

def press(key):
    current_text = entry.get()
    if current_text == "0":
        entry.delete(0, tk.END)
        entry.insert(tk.END, key)
    else:
        entry.insert(tk.END, key)

def evaluate():
    try:
        current_text = entry.get()
        result = eval(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)
    entry.insert(tk.END, "0")

window = tk.Tk()
window.title("My Calculator")
window.configure(bg='dark grey')

entry = tk.Entry(window, width=30, font=('Times New Roman', 20), bd=15, insertwidth=1, justify='right', bg='white')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
entry.insert(0, "0")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(window, text=button, padx=10, pady=10, font=('Times New Roman', 15), bd=5, bg='dark grey', fg='white', command=evaluate)
    else:
        btn = tk.Button(window, text=button, padx=10, pady=10, font=('Times New Roman', 15), bd=5, bg='grey', fg='white', command=lambda b=button: press(b))
    btn.grid(row=row, column=col, sticky='nsew')
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(window, text='Clear', padx=10, pady=10, font=('Times New Roman', 15), bd=5, bg='grey', fg='white', command=clear)
clear_button.grid(row=row, column=col, columnspan=4, sticky='nsew')

for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
