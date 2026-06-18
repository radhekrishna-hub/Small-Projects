from tkinter import *
import random
import string

win = Tk()

win.geometry("400x520")
win.title("Random Password Generator")
win.resizable(False,False)

title1 = Label(win, text="Random Password Generator",padx=50,pady=50,font="comicsansms 19 bold")
title1.pack()


def generate_pass():
    n = name1.get()
    d = dob1.get()
    p = phone1.get()
    a = age1.get()
    n = n.capitalize()
    n_part = n[:3]
    phone_part = "".join(random.sample(p,2))

    specials = "@#$%&!"
    special = random.choice(specials)
    
    dob_digits = ""

    for ch in d:
        if ch.isdigit():
            dob_digits += ch
    
    year = dob_digits[-4:]

    password = n_part + year + special + phone_part + a

    return password



def generate_random_pass():
    length = random.randint(8, 12)

    # First character must be capital
    first_char = random.choice(string.ascii_uppercase)

    # Mandatory characters
    chars = [
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Remaining characters
    pool = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 3):
        chars.append(random.choice(pool))

    # Shuffle everything except first character
    random.shuffle(chars)

    # Final password
    password = first_char + "".join(chars)

    return password

def random_generate_pass_button():
    password = generate_random_pass()

    generatedd1.delete(0, "end")
    generatedd1.insert(0, password)

def generate_pass_button():
    password = generate_pass()

    generated1.delete(0, "end")
    generated1.insert(0, password)



fr = Frame(win)
fr.pack(pady=10)


name = Label(fr, text="Name")
name.grid(row=0, column=0, padx=10, pady=10)

name1 = Entry(fr, width=30)
name1.grid(row=0, column=1, padx=10, pady=10)

dob = Label(fr, text="Date of Birth")
dob.grid(row=1, column=0, padx=10, pady=10)

dob1 = Entry(fr, width=30)
dob1.grid(row=1, column=1, padx=10, pady=10)

phone = Label(fr, text="Phone number")
phone.grid(row=2, column=0, padx=10, pady=10)

phone1 = Entry(fr, width=30)
phone1.grid(row=2, column=1, padx=10, pady=10)

age = Label(fr, text="Age")
age.grid(row=3, column=0, padx=10, pady=10)

age1 = Entry(fr, width=30)
age1.grid(row=3, column=1, padx=10, pady=10)

# Button
# clr = Button(fr, text="Clear",justify=CENTER,command=clear, bg="light green",padx=20)
# clr.grid(row= 4, column=0, padx=10, pady=10)

generate = Button(fr, text="Generate Password",justify=CENTER,command=generate_pass_button,padx=37, bg="light green")
generate.grid(row= 4, column=1, padx=10, pady=10)

generated = Label(fr, text="Generated Password ")
generated.grid(row=5, column=0, padx=10, pady=10)

generated1 = Entry(fr, width=40)
generated1.grid(row=5, column=1, padx=10, pady=10)

between = Label(win, text="OR")
between.pack()

fra = Frame(win)
fra.pack()

generatedd = Label(fra, text="Random Password ",padx=10)
generatedd.pack(side=LEFT)
generatedd1 = Entry(fra, width=90)
generatedd1.pack(side=LEFT,padx=19,pady=10)

generate_ran = Button(win, text="Generate Random Password",justify=CENTER,command=random_generate_pass_button,padx=37, bg="light green")
generate_ran.pack()

win.mainloop()
