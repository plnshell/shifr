from tkinter import *
from tkinter import messagebox

alphabet_for_cesar = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet_en = "abcdefghijklmnopqrstuvwxyz"


def encryption():
    global alphabet_en
    e = encryption_method.get()
    result = ""
    message = str(message_enter.get()).lower()
    for i in message:
        if i in alphabet_en:
            messagebox.showerror("Warning", "Требуется ввести сообщение на кириллице")
            message = ''
            message_enter.set('')
            break

    if e == 1:
        try:
            key = int(key_enter.get())
            global alphabet_for_cesar

            for i in range(0, len(message)):

                if message[i] in alphabet_for_cesar:
                    b = alphabet_for_cesar[alphabet_for_cesar.index(message[i]) + key]
                    result += b

            my_string_var.set(result)

        except ValueError:
            messagebox.showerror("Warning", "Требуется ввести число в поле ключ")
            key_enter.set('')


    elif e == 2:

        key = str(key_enter.get())
        if key.isalpha():
            c = 0
            matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [3, 3, 3, 3, 3, 3, 3, 3]]
            global alphabet

            for q in alphabet:
                if q not in key:
                    key += q

            for i in range(0, 4):
                for j in range(0, 8):
                    if c == len(key):
                        break
                    if key[c] not in matrix:
                        matrix[i][j] = key[c]
                    c += 1

            for w in message:
                for i in range(0, 4):
                    for j in range(0, 8):
                        if w == matrix[i][j]:
                            if i == 3:
                                result += matrix[0][j]
                            else:
                                result += matrix[i + 1][j]

            my_string_var.set(result)

        else:
            messagebox.showerror("Warning", "Требуется ввести слово в поле ключ")
            key_enter.set('')

    elif e == 3:
        key = str(key_enter.get())
        if key.isalpha():
            c = 0
            leng = int((len(message) / len(key)) + 1)
            key_1 = key * leng

            for i in message:
                z = alphabet_for_cesar.index(key_1[c])
                y = alphabet_for_cesar.index(i)
                c += 1
                result += alphabet_for_cesar[z + y]
            my_string_var.set(result)
        else:
            messagebox.showerror("Warning", "Требуется ввести слово в поле ключ")
            key_enter.set('')


def decoding():
    e = encryption_method.get()
    result = ""
    message = str(message_enter.get()).lower()
    for i in message:
        if i in alphabet_en:
            messagebox.showerror("Warning", "Требуется ввести сообщение на кириллице")
            message = ''
            message_enter.set('')
            break

    if e == 1:
        try:
            key = int(key_enter.get())
            global alphabet_for_cesar

            for i in range(0, len(message)):

                if message[i] in alphabet_for_cesar:
                    b = alphabet_for_cesar[alphabet_for_cesar.index(message[i]) - key]
                    result += b

            my_string_var.set(result)
        except ValueError:
            messagebox.showerror("Warning", "Требуется ввести число в поле ключ")
            key_enter.set('')

    elif e == 2:

        key = str(key_enter.get())
        if key.isalpha():
            c = 0
            matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [3, 3, 3, 3, 3, 3, 3, 3]]
            global alphabet

            for q in alphabet:
                if q not in key:
                    key += q

            for i in range(0, 4):
                for j in range(0, 8):
                    if c == len(key):
                        break
                    if key[c] not in matrix:
                        matrix[i][j] = key[c]
                    c += 1

            for w in message:
                for i in range(0, 4):
                    for j in range(0, 8):
                        if w == matrix[i][j]:
                            if i == 0:
                                result += matrix[3][j]
                            else:
                                result += matrix[i - 1][j]
            my_string_var.set(result)
        else:
            messagebox.showerror("Warning", "Требуется ввести слово в поле ключ")
            key_enter.set('')

    elif e == 3:
        key = str(key_enter.get())
        if key.isalpha():
            c = 0
            leng = int((len(message) / len(key)) + 1)
            key_1 = key * leng

            for i in message:
                z = alphabet_for_cesar.index(key_1[c])
                y = alphabet_for_cesar.index(i)
                c += 1
                result += alphabet_for_cesar[y - z]

            my_string_var.set(result)
        else:
            messagebox.showerror("Warning", "Требуется ввести слово в поле ключ")
            key_enter.set('')


root = Tk()
root.title('shifr')
root.geometry("300x350")

header = Label(text="Выберите метод шифрования", padx=15, pady=10)
header.grid(row=0, column=0, sticky=E)

encryption_method = IntVar()

Radiobutton(text="Цезарь", variable=encryption_method, value=1).grid(row=1, column=0)
Radiobutton(text="Трисемус", variable=encryption_method, value=2).grid(row=2, column=0)
Radiobutton(text="Вижинер", variable=encryption_method, value=3).grid(row=3, column=0)

Label(text="Введите ключ", padx=15, pady=10).grid(row=4, column=0, sticky=W)

key_enter = StringVar()
key_entry = Entry(textvariable=key_enter).grid(row=5)

Label(text="Введите сообщение", padx=15, pady=10).grid(row=6, column=0, sticky=W)

message_enter = StringVar()
message_entry = Entry(textvariable=message_enter).grid(row=7)

message_button = Button(text="Зашифровать", command=encryption, pady=1).grid(row=8, column=0, sticky=W)
message_button = Button(text="Расшифровать", command=decoding, pady=1).grid(row=8, column=1, sticky=W)

my_string_var = StringVar()
my_string_var.set("")

sel = Entry(textvariable=my_string_var).grid(row=10, column=0, sticky=E)

root.mainloop()