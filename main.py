import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Star Wars Miniatures Manager')

# Database

# Connect to database
with sqlite3.connect('minis-db') as db:
    cursor = db.cursor()



# Commit changes
db.commit()

# Close connection
db.close()

# Run program
root.mainloop()
