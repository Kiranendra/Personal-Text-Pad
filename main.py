from tkinter import *
from sqlite3 import connect


def encrypt_text(text):
    encrypted_text = ""
    for letter in text:
        encrypted_text += chr(ord(letter) + 5)
        
    return encrypted_text


def decrypt_text(text):
    decrypted_text = ""
    for letter in text:
        decrypted_text += chr(ord(letter) - 5)
        
    return decrypted_text


def create_table():
    con = connect('personal.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS personal (data TEXT)")
    cur.close()
    con.close()
    

def exit_func():
    user_text = text.get("1.0", END).strip()
    con = connect('personal.db')
    cur = con.cursor()
    create_table()
    encrypted_text = encrypt_text(user_text)
    cur.execute("DELETE FROM personal")
    cur.execute("INSERT INTO personal (data) VALUES (?)", (encrypted_text, ))
    con.commit()
    cur.close()
    con.close()
    window.destroy()
    

def read_data():
    create_table()
    con = connect('personal.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM personal")
    data = cur.fetchall()
    i = 1.0
    for row in data:
        txt = ""
        for r in row:
            txt = r.replace("{","")
            txt = r.replace("}","")
        text.insert(i, decrypt_text(txt))
        i += float(len(row))
    
    cur.close()
    con.close()


def text_window():
    global window
    window = Tk()
    window.title("My Pad")
    window.geometry("400x400")
    scroll = Scrollbar(window)
    scroll.pack(side=RIGHT, fill=Y)
    global text
    text = Text(window, yscrollcommand=scroll.set)
    text.pack(fill=BOTH)
    read_data()
    scroll.config(command=text.yview)
    window.protocol("WM_DELETE_WINDOW", exit_func)
    window.mainloop()


def get_password():
    global label_value, password_value
    my_password = '1234'
    password = password_value.get().strip()
    if password == "":
        label_value.set("Please enter a password")
    elif password != my_password:
        password_value.set("")
        label_value.set("Wrong password")
    else:
        global root
        root.destroy()
        text_window()


root = Tk()
root.title("Validate Yourself")
root.maxsize(250, 80)
root.minsize(250, 80)

label = Label(root, text="Enter Password : ", font="arial 10", padx=3, pady=5)
label.grid(row=0, column=1)

password_value = StringVar()
password_entry = Entry(root, textvariable=password_value)
password_entry.grid(row=0, column=2)

button = Button(root, text="Enter", command=get_password)
button.grid(row=1, column=1, columnspan=3)

label_value = StringVar()
label_value.set("Enter Password")
label = Label(root, textvariable=label_value, padx=3, pady=5, fg="red")
label.grid(row=2, column=1, columnspan=3)

root.mainloop()
