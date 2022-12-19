from tkinter import *
import tkinter
import math
import random
import string_utils

root = Tk()
padd = 50 # creating variable for spaces
root['padx']=padd # makes the spaces
root.title('Password Generator')
root.geometry("230x180")

clicked = StringVar()# whats clicked on a checkbox

chk1 = tkinter.IntVar() # check boxes
chk2 = tkinter.IntVar() #
chk3 = tkinter.IntVar() #

def password_generate(leng): # function that creates the password that jumbles and puts together the letters

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"

    if chk1.get() and chk2.get() and chk3.get():
        qty = leng/3
        if isinstance(qty, float):
            qty1 = math.ceil(qty)
            qty2 = round(qty)
            qty34 = qty1 + qty2
            qty3 = leng - qty34
            password1 = "".join(random.sample(uppercase_letters, qty1))
            password2 = "".join(random.sample(lowercase_letters, qty2))
            password3 = "".join(random.sample(numbers, qty3))
            password5 = password1 + password2 + password3
            password4 = string_utils.shuffle(password5)
        else:
            password1 = "".join(random.sample(uppercase_letters, qty))
            password2 = "".join(random.sample(lowercase_letters, qty))
            password3 = "".join(random.sample(numbers, qty))
            password5 = password1 + password2 + password3
            password4 = string_utils.shuffle(password5)
    elif chk1.get() and chk2.get():
        qty = leng/2
        if isinstance(qty, float):
            qty1 = math.ceil(qty)
            qty2 = leng - qty1
            password1 = "".join(random.sample(uppercase_letters, qty1))
            password2 = "".join(random.sample(lowercase_letters, qty2))
            password3 = password1 + password2
            password4 = string_utils.shuffle(password3)
        else:
            password1 = "".join(random.sample(uppercase_letters, qty))
            password2 = "".join(random.sample(lowercase_letters, qty))
            password3 = password1 + password2
            password4 = string_utils.shuffle(password3)
    elif chk1.get() and chk3.get():
        qty = leng/2
        if isinstance(qty, float):
            qty1 = math.ceil(qty)
            qty3 = leng - qty1
            password1 = "".join(random.sample(uppercase_letters, qty1))
            password2 = "".join(random.sample(numbers, qty3))
            password3 = password1 + password2
            password4 = string_utils.shuffle(password3)
        else:
            password1 = "".join(random.sample(uppercase_letters, qty))
            password2 = "".join(random.sample(numbers, qty))
            password3 = password1 + password2
            password4 = string_utils.shuffle(password3)
    elif chk2.get() and chk3.get():
        qty = leng/2
        if isinstance(qty, float):
            qty2 = math.ceil(qty)
            qty3 = leng - qty2
            password1 = "".join(random.sample(lowercase_letters, qty2))
            password2 = "".join(random.sample(numbers, qty3))
            password3 = password1 + password2
            password4 = string_utils.shuffle(password3)
        else:
            password1 = "".join(random.sample(lowercase_letters, qty))
            password2 = "".join(random.sample(numbers, qty))
            password3 = password1 + password2
            password4 = string_utils.shuffle(password3)
    elif chk1.get():
        password4 = "".join(random.sample(uppercase_letters, leng))
    elif chk2.get():
        password4 = "".join(random.sample(lowercase_letters, leng))
    elif chk3.get():
        password4 = "".join(random.sample(numbers, leng))
    else:
        password4 = "".join(random.sample(uppercase_letters, leng))

    display_result.delete(0, tkinter.END)
    display_result.insert(0, password4)

def checkbox_check():

    if clicked.get() == '3':
        password_generate(3)
    elif clicked.get() == '4':
        password_generate(4)
    elif clicked.get() == '5':
        password_generate(5)
    elif clicked.get() == '6':
        password_generate(6)
    elif clicked.get() == '7':
        password_generate(7)
    elif clicked.get() == '8':
        password_generate(8)
    else:
        password_generate(9)

drop = OptionMenu(root, clicked, '3', '4', '5', '6', '7', '8')
drop.pack()
drop.grid(row=2,column=6)

title_text = tkinter.Label(text='Password Generator') # title of window
title_text.grid(row=0, column=6) # where you want teh title
display_result = tkinter.Entry() #
display_result.grid(row=1, column=6) # where you want to display the result
chkone = tkinter.Checkbutton(text='Uppercase letters', onvalue=1, offvalue=0, variable=chk1) # the 6 character buttun
chkone.grid(row=3, column=6)
chktwo = tkinter.Checkbutton(text='Lowercase letters', onvalue=1, offvalue=0, variable=chk2) # the 6 character buttun
chktwo.grid(row=4, column=6)
chkthree = tkinter.Checkbutton(text='Numbers', onvalue=1, offvalue=0, variable=chk3) # the 6 character buttun
chkthree.grid(row=5, column=6)
pass_generate = tkinter.Button(text='Generate', command=checkbox_check)
pass_generate.grid(row=6, column=6)
root.mainloop()

