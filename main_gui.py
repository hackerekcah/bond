from Tkinter import *


def get_t(interest_day, interest_month, buy_date):
    from datetime import date
    buy_date_ = date(*[int(x) for x in buy_date.split('-')])
    try:
        interest_date_ = date(buy_date_.year, interest_month, interest_day)
    except ValueError:
        import tkMessageBox
        tkMessageBox.showinfo("Alert", "Not a valid interest date! Set same as Buy date")
        interest_mont_str.set(str(buy_date_.month))
        interest_day_str.set(str(buy_date_.day))
        return 0

    delta_day = interest_date_ - buy_date_

    delta_day_int = delta_day.days

    if delta_day_int < 0:
        t = (360 + delta_day_int) / 360.0
    elif delta_day_int == 0:
        t = 0
    else:
        t = delta_day_int / 360.0

    return t


def on_ytm():
    p0 = float(p0_str.get())
    p1 = float(p1_str.get())
    n = int(n_str.get())
    c = float(c_str.get()) * 0.01
    interest_month = int(interest_mont_str.get())
    interest_day = int(interest_day_str.get())
    buy_date = buydate_picker.current_text
    if buy_date == "":
        import tkMessageBox
        tkMessageBox.showinfo("Alert", "Pick a Buy Date!")
        return
    t = get_t(interest_day, interest_month, buy_date)
    from bond import calc_ytm
    new_ytm = calc_ytm(p0, p1, n, c, t)
    ytm_str.set(str(new_ytm * 100))
    ytm_entry.focus()

def on_c():
    p0 = float(p0_str.get())
    p1 = float(p1_str.get())
    n = int(n_str.get())
    ytm = float(ytm_str.get()) * 0.01
    interest_month = int(interest_mont_str.get())
    interest_day = int(interest_day_str.get())
    buy_date = buydate_picker.current_text
    if buy_date == "":
        import tkMessageBox
        tkMessageBox.showinfo("Alert", "Pick a Buy Date!")
        return
    t = get_t(interest_day, interest_month, buy_date)

    from bond import calc_c
    new_c = calc_c(p0, p1, ytm, n, t)
    c_str.set(str(new_c * 100))
    c_entry.focus()

def on_p0():
    p1 = float(p1_str.get())
    n = int(n_str.get())
    ytm = float(ytm_str.get()) * 0.01
    c = float(c_str.get()) * 0.01
    interest_month = int(interest_mont_str.get())
    interest_day = int(interest_day_str.get())
    buy_date = buydate_picker.current_text
    if buy_date == "":
        import tkMessageBox
        tkMessageBox.showinfo("Alert", "Pick a Buy Date!")
        return
    t = get_t(interest_day, interest_month, buy_date)

    from bond import calc_p0
    new_p0 = calc_p0(p1, c, ytm, n, t)
    p0_str.set(str(new_p0))
    p0_entry.focus()

def on_p1():
    p0 = float(p0_str.get())
    n = int(n_str.get())
    ytm = float(ytm_str.get()) * 0.01
    c = float(c_str.get()) * 0.01
    interest_month = int(interest_mont_str.get())
    interest_day = int(interest_day_str.get())
    buy_date = buydate_picker.current_text
    if buy_date == "":
        import tkMessageBox
        tkMessageBox.showinfo("Alert", "Pick a Buy Date!")
        return
    t = get_t(interest_day, interest_month, buy_date)

    from bond import calc_p1
    new_p1 = calc_p1(p0, c, ytm, n, t)
    p1_str.set(str(new_p1))
    p1_entry.focus()


root = Tk()
root.title("Bond Calculator")
root.minsize(width=400, height=400)
row_index = 0

p0_label = Label(root, text='{:10s}'.format('Present Price P0:'))
p0_label.grid(row=row_index)

p0_str = StringVar()
p0_entry = Entry(root, textvariable= p0_str)
p0_str.set('950')
p0_entry.grid(row=row_index,column=1)

row_index += 1
p1_label = Label(root, text='{:10s}'.format('Par Price P1:'))
p1_label.grid(row=row_index)

p1_str = StringVar()
p1_entry = Entry(root, textvariable= p1_str)
p1_str.set('1000')
p1_entry.grid(row=row_index, column=1)

row_index += 1
c_label = Label(root, text='{:10s}'.format('Coupon Rate C(%):'))
c_label.grid(row=row_index)

c_str = StringVar()
c_entry = Entry(root, textvariable= c_str)
c_str.set('7')
c_entry.grid(row=row_index, column=1)


row_index += 1
n_label = Label(root, text='{:10s}'.format('Years to Maturity N:'))
n_label.grid(row=row_index)

n_str = StringVar()
n_entry = Entry(root, textvariable=n_str)
n_str.set('5')
n_entry.grid(row=row_index, column=1)

row_index += 1
ytm_label = Label(root, text='{:10s}'.format('Yield to Maturity YTM(%):'))
ytm_label.grid(row=row_index)

ytm_str = StringVar()
ytm_entry = Entry(root, textvariable=ytm_str)
ytm_str.set('0.7')
ytm_entry.grid(row=row_index, column=1)


row_index += 1

buydate_label = Label(root, text='{:10s}'.format('Buy Date:'))
buydate_label.grid(row = row_index)
from datepicker import Datepicker
buydate_picker = Datepicker(root)
buydate_picker.grid(row = row_index, column=1)

row_index += 1

interest_mont_label = Label(root, text='{:10s}'.format('Interest Month:'))
interest_mont_label.grid(row = row_index)

interest_mont_str = StringVar()
interest_mont_entry = Entry(root, textvariable=interest_mont_str)
interest_mont_str.set('10')
interest_mont_entry.grid(row=row_index, column=1)

row_index += 1

interest_day_label = Label(root, text='{:10s}'.format('Interest Day:'))
interest_day_label.grid(row = row_index)

interest_day_str = StringVar()
interest_day_entry = Entry(root, textvariable=interest_day_str)
interest_day_str.set('1')
interest_day_entry.grid(row=row_index, column=1)

row_index += 1
ytm_button = Button(root, text='calculate Yield To Maturity', bg='pink', command=on_ytm)
ytm_button.grid(row=row_index)

row_index += 1
c_button = Button(root, text='calculate Coupon Rate', bg='pink', command=on_c)
c_button.grid(row=row_index)

row_index += 1
p0_button = Button(root, text='calculate P0', bg='pink', command=on_p0)
p0_button.grid(row=row_index)

row_index += 1
p1_button = Button(root, text='calculate P1', bg='pink', command=on_p1)
p1_button.grid(row=row_index)

mainloop()