import tkinter as tk


def add_digit(digit):
    if work.get() == '0':
        work.delete(0, tk.END)
        work.insert(0, str(digit))
    else:
        if digit != 0:
            value = work.get() + str(digit)
            work.delete(0, tk.END)
            work.insert(0, value)
        else:
            value = work.get() + str(digit)
            check = []
            word = ''
            signs = []
            res = ''
            i = 0
            while i < len(value):
                if value[i] not in '+-*/':
                    word += value[i]
                else:
                    signs.append(value[i])
                    check.append(word)
                    word = ''
                i += 1
            check.append(word)
            j = 0
            while j < len(check) - 1:
                if check[j].startswith('0'):
                    continue
                else:
                    res += check[j]
                    res += signs[j]
                j += 1
            if not check[-1].startswith('0'):
                res += check[-1]
            work.delete(0, tk.END)
            work.insert(0, res)


def add_sign(sign):
    value = work.get()
    if value[-1] == '+' or value[-1] == '-' or value[-1] == '*' or value[-1] == '/':
        work.delete(0, tk.END)
        work.insert(0, value[:len(value) - 1] + sign)
    else:
        work.delete(0, tk.END)
        work.insert(0, value + sign)


def finish():
    value = work.get()
    if value[-1] == '-' or value[-1] == '+' or value[-1] == '*' or value[-1] == '/':
        work.delete(0, tk.END)
        work.insert(0, value)
    else:
        res = eval(value)
        work.delete(0, tk.END)
        work.insert(0, res)


def make_digit_btn(digit):
    return tk.Button(win, text=str(digit), font=('Arial', 28, 'bold'), foreground='#524681', relief='raised',
                     background='white', bd=3, command=lambda: add_digit(digit))


def make_sign_btn(sign):
    return tk.Button(win, text=sign, font=('Arial', 28, 'bold'), foreground='#7C1313', background='white', bd=3,
                     command=lambda: add_sign(sign))


def delete():
    value = work.get()
    work.delete(0, tk.END)
    work.insert(0, value[:len(value) - 1])


win = tk.Tk()
win.title('Calculator')
win.geometry('400x500+50+50')
win.resizable(False, False)
win.config(bg='#C8D2FD')

photo = tk.PhotoImage(file='keys.png')
win.iconphoto(False, photo)

work = tk.Entry(win, font=('Arial', 24, 'bold'), justify=tk.RIGHT, foreground='#524681')
work.grid(row=0, column=0, columnspan=4, stick='wens', padx=10, pady=10)
work.insert(0, '0')

make_digit_btn(1).grid(row=1, column=0, stick='wens', padx=10, pady=10)
make_digit_btn(2).grid(row=1, column=1, stick='wens', padx=10, pady=10)
make_digit_btn(3).grid(row=1, column=2, stick='wens', padx=10, pady=10)
make_digit_btn(4).grid(row=2, column=0, stick='wens', padx=10, pady=10)
make_digit_btn(5).grid(row=2, column=1, stick='wens', padx=10, pady=10)
make_digit_btn(6).grid(row=2, column=2, stick='wens', padx=10, pady=10)
make_digit_btn(7).grid(row=3, column=0, stick='wens', padx=10, pady=10)
make_digit_btn(8).grid(row=3, column=1, stick='wens', padx=10, pady=10)
make_digit_btn(9).grid(row=3, column=2, stick='wens', padx=10, pady=10)
make_digit_btn(0).grid(row=4, column=0, stick='wens', padx=10, pady=10)

make_sign_btn('+').grid(row=2, column=3, stick='wens', padx=10, pady=10)
make_sign_btn('-').grid(row=3, column=3, stick='wens', padx=10, pady=10)
make_sign_btn('*').grid(row=4, column=1, stick='wens', padx=10, pady=10)
make_sign_btn('/').grid(row=4, column=2, stick='wens', padx=10, pady=10)

tk.Button(win, text='<=', font=('Arial', 28, 'bold'), foreground='#7C1313', background='white', bd=3,
          command=delete).grid(row=1,
                               column=3,
                               stick='wens',
                               padx=10,
                               pady=10)
tk.Button(win, text='=', font=('Arial', 28, 'bold'), foreground='#7C1313', background='white', bd=3,
          command=finish).grid(row=4,
                               column=3,
                               stick='wens',
                               padx=10,
                               pady=10)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=100)

win.grid_rowconfigure(0, minsize=100)
win.grid_rowconfigure(1, minsize=100)
win.grid_rowconfigure(2, minsize=100)
win.grid_rowconfigure(3, minsize=100)
win.grid_rowconfigure(4, minsize=100)

win.mainloop()
