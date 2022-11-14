import requests
import json
from tkinter import Tk, ttk
from tkinter import * 
from PIL import Image, ImageTk

cor0 = '#FFFFFF'
cor1 = '#333333'
cor2 = '#FF00FF'

window = Tk()
window.geometry('300x320')
window.title('Currency Exchange')
window.configure(bg=cor0)
window.resizable(height=FALSE, width=FALSE)

top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

# logic

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    if currency_2 == 'GBP':
        symbol ='£'
    elif currency_2 == 'RUB':
        symbol = '₽'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'KZT':
        symbol = '₸'
    elif currency_2 == 'USD':
        symbol = '$'

    headers = {
	    "X-RapidAPI-Key": "8daf4e43e0msh92d871d190888c5p1cefddjsn415251d90377",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data['result']['convertedAmount']
    formatted = symbol + '{:,.2f}'.format(converted_amount)

    result['text'] = formatted
    print(converted_amount, formatted)

# logic

icon = Image.open('images/icon2.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text = 'Currency Exchange', height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=cor2,fg=cor0)
app_name.place(x=0, y=0)

result = Label(main, text = ' ', width=16, height=2, relief='solid', pady=7, anchor=CENTER, font=('Ivy 15 bold'), bg=cor0,fg=cor1)
result.place(x=50, y=10)

currency = ['GBP', 'RUB', 'EUR', 'KZT', 'USD']

from_label = Label(main, text = 'From', width=8, height=1, relief='flat', pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=cor0,fg=cor1)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text = 'To', width=8, height=1, relief='flat', pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=cor0,fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text='Exchange', width=19, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), command=convert)
button.place(x=50, y=210)

window.mainloop()