
from cProfile import label
from logging import root
from tkinter import *
import calendar
from tkinter.font import BOLD, ITALIC


year_input = int(input("enter year:"))

root = Tk()
root.geometry("1200x800")
root.title("calendar")
root.configure(background="#66ff00")



a = calendar.calendar(year_input) 


l1 = Label(root,padx=100,background="#66ff00")
l1.grid(row=1,column=1)


l2 = Label(root,padx=100,background="#66ff00")
l2.grid(row=2,column=1)


l2 = Label(root,padx=45,pady=400,background="black")
l2.grid(row=1,column=5,rowspan=10)


l2 = Label(root,padx=45,pady=400,background="black")
l2.grid(row=1,column=3,rowspan=10)


label_title= Label(root,text="***calendar***",font = ("ALGERIAN",60,BOLD,ITALIC), foreground="red",background="black",padx=50)
label_title.grid(row=1,column=4)


label_calendar = Label(root,text=a,background="#66ff66",foreground="black" ,padx=20,font = ("ALGERIAN",13,BOLD))
label_calendar.grid(row=2,column=4)







    
            
    


        
        
root.mainloop()        