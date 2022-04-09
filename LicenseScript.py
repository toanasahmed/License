from firebase import firebase
from firebase_admin import db
from getmac import get_mac_address as gma
import datetime
from tkinter import messagebox
import os
from tkinter import *
import inventory_manager
expiryVariable = 0

gui=Tk()
gui.overrideredirect(1)
gui.withdraw()
#photo = PhotoImage(file="logo.png")
#gui.iconphoto(False, photo)

def guifun():
    global photo, e1
    gui = Tk()
    gui.geometry("400x220")
    gui.maxsize(400, 220)
    gui.title("Register Your PC")
    l1 = Label(gui, text="Enter your name", font=("times 12 bold"))
    l1.place(x=30, y=50)
    
    e1 = Entry(gui, relief=SUNKEN, bd=5, width=30)
    e1.place(x=180, y=50)

    btn = Button(gui, text="submit",bg="green",command=feedback)
    btn.place(x=220, y=150)

    address = gma()
    #print('address', address)
    gui.mainloop()



def feedback():
    global e1, firebase;
    ex1= e1.get()
    messagebox.showinfo("Info", "Congratulations, Your request is received")
    firebase.put('requested/', str(ex1), address)

    print(ex1)

def networkdialog():

    gui.overrideredirect(1)
    gui.withdraw()
    messagebox.showerror("Error", "please check your internet connection")
    gui.destroy()
    os._exit(1)

def validationcheck():
    global validationcheck, validationVariable

    global val_i, value, expiryVariable
    validationVariable = 0
    if expiryVariable == 0:
        validationVariable = 0
        if value == None:
            validationVariable = 1
            val_i = 0
            answer=messagebox.showerror("Error", "you are not registered please registered your self")
            print(answer)
            if answer=="ok":
                guifun()
    

def trialCheck():
    global expiry, today, expiryVariable
    expiryVariable = 0
    try:
        if int(today[2]) >  int(expiry[2]):
            answer=messagebox.showerror("Error", "Your trial has been expired")
            expiryVariable = 1
        elif int(today[2]) ==  int(expiry[2]):
            if int(today[1]) >  int(expiry[1]):
                answer=messagebox.showerror("Error", "Your trial has been expired")
                expiryVariable = 1
            elif int(today[1]) ==  int(expiry[1]):
                if int(today[0]) >  int(expiry[0]):
                    answer=messagebox.showerror("Error", "Your trial has been expired")
                    expiryVariable = 1
    except:
        answer=messagebox.showerror("Error", "you are not registered please registered your self")
        if answer=="ok":
                guifun()
    
def mainfunction():
    #inventory_manager.main()
    print("Code is working")

address = gma()
#print('address', address)
a = 0
current_time = datetime.datetime.now()
current_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
today = str(current_time).split(" ")
today = today[0]
today = str(today).split("/")

my_str = StringVar()

try:
    #global expiryVariable, validationVariable
    firebase = firebase.FirebaseApplication('https://########.########.########/', None)        #Firebase RTDB URL
    firebase.put('approved/', str(a), current_time)
    value = firebase.get('approved/', address)
    expiry = firebase.get('approved/', 'Expiry')
    expiry = str(value).split("/")
    #print("ADDRESS FOUND", value)
    #print("Expiry", expiry)
    trialCheck()
    validationcheck()
    if validationVariable == 0 and expiryVariable == 0:
        mainfunction()
    #print('done with validation check')
    movetomain = 1

except:
   networkdialog()




