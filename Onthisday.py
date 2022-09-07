from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("300x200+600+250")
root.config(background="#E0FFFF")
# root.resizable(False,False)
root.geometry("755x400")


def dayText(event):
    e1.delete(0, END)
    usercheck = True


def monthText(event):
    e2.delete(0, END)
    passcheck = True


a = StringVar()
b = StringVar()
usercheck = False
passcheck = False

Label(root, text="Day", bg="#E0FFFF").place(x=20, y=50)
e1 = Entry(root, textvariable=a)
e1.place(x=100, y=50)
e1.insert(0, "Enter Day")
e1.bind("<Button>", dayText)

Label(root, text="Month", bg="#E0FFFF").place(x=20, y=95)
e2 = Entry(root, textvariable=b)
e2.place(x=100, y=95)
e2.insert(0, "Enter Month")
e2.bind("<Button>", monthText)


def getData(date, month):
    #date = str(19)
    #month = 'february'
    url = 'https://www.onthisday.com/day/' + month + '/' + date
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    text1 = ""
    text1 = soup.title.text + "\nImportant Events\n"
    # Important Events
    divs = soup.find_all('ul', class_='event-list event-list--with-advert')
    for i in divs:
        text1 += i.text

    # Famous birthdays
    text1 = text1 + "\nFamous Birthdays\n"
    birthdays = soup.find('ul', class_='photo-list')
    bdays = birthdays.find_all('li')
    for i in bdays:
        text1 += i.text
    # This day in movies, music and sports
    check = soup.find_all('section', class_='grid__item one-half--1024')
    for i in check:
        text1 += i.text
    # Random fact on this day
    did_you_know = soup.find('section', class_='section section--highlight section--did-you-know')
    text1 += did_you_know.text

    answer.insert(END, text1)


answer = Text(root, foreground='blue', font=('Comic Sans MS', 12), width=44, height=15)
answer.place(x=260, y=10)

b1 = Button(text="Get", font=('Comic Sans MS', 10), width=24, command=lambda: getData(e1.get(), e2.get())).place(x=50,
                                                                                                                 y=140)

root.mainloop()
