
# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
import sys
sys.path.insert(0, "../Backend/Classes")
from DatabaseHandler import DatabaseHandler

# Create Object
root = Tk()

# Set geometry
root.geometry("800x800")


#Obtin ziua de astazi 
current_date = datetime.now()
# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = current_date.year, month = current_date.month,
               day = current_date.day,maxdate = current_date,showothermonthdays = False,date_pattern = "YYYY-MM-DD")

cal.pack(pady = 20)

#nevoie de un buton care face asta 
#db = DatabaseHandler("../Backend/Data/Database.sqlite")
#db.CreateTable()
#db.InsertDate(f" '{(str)(cal.get_date())}' ")
#nevoie de un buton care face asta 

db = DatabaseHandler("../Backend/Data/Database.sqlite")
db.CreateTable()

def insert():
    db.InsertDate(f" '{(str)(cal.get_date())} ' ")

Bt = Button(root,text="salveaza data",activebackground="green",command = insert())
Bt.pack(padx=20, pady=20)

print(f" '{(str)(cal.get_date())} ' ")
# Execute Tkinter
root.mainloop()



