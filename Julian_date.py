import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from time import sleep
#  MINI PROJECT TITLE ; Team 1

""" Write a function which checks whether a given year is prime.
    Write a function to validate a given date – use the former function to check for prime.
    Write a function to convert a given date to Julian Date.
        1 st March 2013 => 31 + 28 + 1 => 60 th day of the year
        1 st March 2016 => 31+ 29 + 1 => 61 st day of the year"""


def date_input():
    # Globalising all the required variables
    global date, dd, mm, yyyy, date1, days, days_in_month

    date = input()

    # Copying the value of variable "date" to "date1" for later use since we are going perform split() on it
    date1 = date

    # Performing if-else condition to check type of input entered by the user to make to more user-friendly
    date = date.split(" ")
    try:  # 1 st March 2000
        dd = int(date[0])
        mm = (date[2]).lower()
        yyyy = int(date[3])

    except:
        try:  # 1 March 2000
            dd = int(date[0])
            mm = (date[1]).lower()
            yyyy = int(date[2])
        except:  # 1st March 2000
            x = date[0]
            dd = int(x[0:-2])
            mm = (date[1]).lower()
            yyyy = int(date[2])

    # Creating a list with no of days in each month respectively from January to December according to a non leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # if statement evaluating if the year entered by the user is leap year
    if (yyyy % 4 == 0) and ((yyyy % 100 != 0) or (yyyy % 400 == 0)):
        days_in_month[1] = 29

    # Assigning month number based on input given by the user
    if mm == "january" or mm == "jan":
        mm = 1
    elif mm == "february" or mm == "feb":
        mm = 2
    elif mm == "march" or mm == "mar":
        mm = 3
    elif mm == "april" or mm == "apr":
        mm = 4
    elif mm == "may":
        mm = 5
    elif mm == "june" or mm == "jun":
        mm = 6
    elif mm == "july" or mm == "july":
        mm = 7
    elif mm == "august" or mm == "aug":
        mm = 8
    elif mm == "september" or mm == "sept" or mm == "sep":
        mm = 9
    elif mm == "october" or mm == "oct":
        mm = 10
    elif mm == "november" or mm == "nov":
        mm = 11
    elif mm == "december" or mm == "dec":
        mm = 12
    # Caution warning to the user if invalid month is entered
    else:
        sleep(1)
        invalid_month()

def invalid_month():
    window2 = Tk()
    window2.geometry('230x120')
    mb.showwarning("Warning", "You've entered an invalid month")

    label1=tk.Label(window2,font='Helvetica 10', text="Do you want to enter the date again? ", borderwidth=3, relief="raised")
    label1.place(relx=0.490, rely=0.375, anchor=CENTER)

    def close_window2():
        window2.destroy()
        exit()

    def date_input1():
        print("Enter the date :- ")
        window2.destroy()
        date_input()

    style3 = Style()
    style4 = Style()

    style3.configure('G.TButton', font =('calibri', 10, 'bold'),background='green',foreground = 'green')
    style4.configure('R.TButton', font =('calibri', 10, 'bold'),background = 'red',foreground = 'red' )

    btn1 = Button(window2, text = 'Yes',style = 'G.TButton',command=date_input1)
    btn1.place(relx=0.3, rely=0.825, anchor=CENTER)

    btn2 = Button(window2, text = 'No',style = 'R.TButton', command=close_window2)
    btn2.place(relx=0.725, rely=0.825, anchor=CENTER)

    window2.mainloop()


# Function to check whether given year is prime or not
def prime(yyyy):
    if yyyy == 1:
        return "The Year you've entered is not prime"
    elif yyyy == 2:
        return "The Year you've entered is prime"
    else:
        for i in range(2, yyyy):
            if yyyy % i == 0:
                return "The Year you've entered is not prime"
        else:
            return "The Year you've entered is prime"


def validate():
    global d
    # Get Max value for a day in given month
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        max_day_value = 31
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        max_day_value = 30
    elif yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0:
        max_day_value = 29
    else:
        max_day_value = 28
    if mm < 1 or mm > 12:
        d = "Date is invalid"
    elif dd < 1 or dd > max_day_value:
        d = "Date is invalid"
    else:
        d = "Valid Date"


# Function to convert a Standard date to Julian date
def std_date_to_jd():
    # Assigning an initial value 0 to the variable
    tot_days_till_month = 0

    # Stores the value of total no of days completed until beginning of this month
    for i in range(mm - 1):
        tot_days_till_month += days_in_month[i]

    # Stores the value of total number of days completed which is the Julian date
    tot_days_till_date = tot_days_till_month + dd

    # Make-up
    if tot_days_till_date % 10 == 1:
        print(date1, "is  ", tot_days_till_date, "st day of the year")

    elif tot_days_till_date % 10 == 2:
        print(date1, "is  ", tot_days_till_date, "nd day of the year")

    elif tot_days_till_date % 10 == 3:
        print(date1, "is  ", tot_days_till_date, "rd day of the year")

    else:
        print(date1, "is  ", tot_days_till_date, "th day of the year")
    print("\n")




def response():
    def f1():
        window.destroy()
        yyyy = int(input("Enter the Year :- "))
        print(prime(yyyy))
        print()
        sleep(1)
        try_again()


    def f2():
        window.destroy()
        print("Enter the date :- ")
        date_input()
        print()
        validate()
        if d == "Valid Date":
            print("The date you've entered is valid")
            print()
        else:
            print("The date you've entered is invalid")
            print()
        sleep(1)
        try_again()
    def f3():
        window.destroy()
        print("Enter the Standard date which should be converted to Julian Date ")
        date_input()
        validate()
        if d == "Valid Date":
            std_date_to_jd()
            sleep(1)
            try_again()
        else:
            print("Looks like the date you've entered is invalid")
            sleep(1)
            try_again()
    def teaminfo():
        mb.showinfo("ABOUT US","SECTION I     TEAM:1    SEM:1\n\nN V RAKESH REDDY:   PES1UG20CS566"
                               "\nSURAJ K M:                 PES1UG20CS599"
                               "\nALMAS BANU:             PES1UG20CS535")
    def rules():
        mb.showinfo("\n Examples of Valid Inputs are :- ",
                    "\n 1 st March 2013 ,           26 th November 2016"
                    "\n 26th November 2011 ,   2nd Jan 2008"
                    "\n 16 June 2010 ,                29 Dec 2020"
                    "\n\n Note: The name of month can be entered in any case ( lower or upper or mixed)"
                    "\n\n For Example :- 'JAN', 'jan','Jan', 'JANUARY','january', 'January' \n ")
    window=tk.Tk()

    window.geometry('975x400')
    window.title("Team-1 (Mini Project)")
    def close_window3 ():
        window.destroy()

    bg=PhotoImage(file="req.png")
    lab=tk.Label(window,font='Helvetica 50', image=bg)
    lab.place(x=0,y=0,relwidth=1,relheight=1)
    b1 = tk.Button(window,text="Find out whether a given year is prime",font="TimesNewRoman 12",bg="black",fg="white",width=35,height=2,command=f1)
    b1.place(relx=0.2, rely=0.25, anchor=CENTER)
    b2 = tk.Button(window,text="Validate a given date",bg="black",font="TimesNewRoman 12",fg="white",width=27,height=2,command=f2)
    b2.place(relx=0.5, rely=0.25, anchor=CENTER)
    b3 = tk.Button(window,text="Convert a standard date to Julian date",font="TimesNewRoman 12",bg="black",fg="white",width=35,height=2,command=f3)
    b3.place(relx=0.8, rely=0.25, anchor=CENTER)
    b4 = tk.Button(window,text="How to Enter the Date",font='Bahnschrift 10',bg="black",fg="white",width=25,height=2,command=rules).place(relx=0.5, rely=0.45, anchor=CENTER)
    b5 = tk.Button (window, text = "ABOUT US",font='Bahnschrift 10',bg="black",fg="white",width=20,height=2, command = teaminfo).place(relx=0.5, rely=0.6, anchor=CENTER)
    b6 = tk.Button (window, text = "QUIT",font='Bahnschrift 10',bg="black",fg="white",width=20,height=2, command = close_window3).place(relx=0.5, rely=0.75, anchor=CENTER)
    window.mainloop()



def try_again():
    window1 = Tk()
    window1.geometry('220x90')

    label1=tk.Label(window1,font='Helvetica 8', text="DO YOU WANT TO TRY AGAIN?").place(relx=0.475, rely=0.3, anchor=CENTER)

    def close_window1():
        window1.destroy()

    def response1():
        close_window1()
        response()

    style1 = Style()
    style2 = Style()

    style1.configure('G.TButton', font =('calibri', 10, 'bold'),background='green',foreground = 'green')
    style2.configure('R.TButton', font =('calibri', 10, 'bold'),background='red',foreground = 'red')

    btn1 = Button(window1, text = 'Yes',style = 'G.TButton',command=response1)
    btn1.place(relx=0.3, rely=0.55, anchor=CENTER)

    btn2 = Button(window1, text = 'No',style = 'R.TButton', command=close_window1)
    btn2.place(relx=0.725, rely=0.55, anchor=CENTER)

    window1.mainloop()

response()

