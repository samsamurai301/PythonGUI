
#import for tkinter package used for GUI implementation
import tkinter as tk

#Set the global variables
global e1
global nsalText

#First option's list to choose in GUI
OptionList_1 = [
    "Day",
    "Hour",
    "Minute",
    "Second",
]

#Second option's list to choose in GUI
OptionList_2 = [
    "Day",
    "Hour",
    "Minute",
    "Second",
]

"""Main function that calculates the conversion of the value inserted in the GUI and returns the result to be displayed. 
It is called when the user presses the Ok button."""
def Ok():
#Error Handling for invalid inputs. 
    try: 
        fr = variable0.get()
        to = variable01.get()
#Convert input to float and do calculations based on the user selections of the lists
        value = float(e1.get())
 
        if (fr == "Day" and to == "Hour"):
            tot = value * 24
        elif (fr == "Day" and to == "Minute"):
            tot = value * 24 * 60
        elif (fr == "Day" and to == "Second"):
            tot = value * 24 * 3600
        elif (fr == "Hour" and to == "Minute"):
            tot = value * 60
        elif (fr == "Hour" and to == "Second"):
            tot = value * 60 * 60
        elif (fr == "Hour" and to == "Day"):
            tot = value / 24
        elif (fr == "Minute" and to == "Second"):
            tot = value * 60
        elif (fr == "Minute" and to == "Hour"):
            tot = value / 60
        elif (fr == "Minute" and to == "Day"):
            tot = value / (24*60)
        elif (fr == "Second" and to == "Minute"):
            tot = value / 60
        elif (fr == "Second" and to == "Hour"):
            tot = value / (60*60)
        elif (fr == "Second" and to == "Day"):
            tot = value / (60*60*24)
        else:
            tot = value
            #Set the final result in the global variable nsalText
        nsalText.set(tot)
#If selection is invalid throw exception and inform the user
    except Exception as e:
        print('This is not a valid number')
        nsalText.set("Invalid Input")
    

#Building of GUI frames and texts
root = tk.Tk()
root.geometry('300x250')
root.title("Time Converver")

labelframe = tk.LabelFrame(root, text="Time Converver System Python")
labelframe.pack(fill="both", expand="yes")

variable0 = tk.StringVar(labelframe)
#Setting the option's list 1
variable0.set(OptionList_1[0])

opt = tk.OptionMenu(labelframe, variable0, *OptionList_1)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")

#Setting the option's list 2
variable01 = tk.StringVar(labelframe)
variable01.set(OptionList_2[0])

opt = tk.OptionMenu(labelframe, variable01, *OptionList_2)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")


nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 13), fg='red')
labelTest.pack(side="top")

#Definig Labelframes text
tk.Label(labelframe, text="From").place(x=10, y=10)
tk.Label(labelframe, text="To").place(x=10, y=40)
tk.Label(labelframe, text="Value").place(x=10, y=80)

tk.Label(labelframe, text="Total:").place(x=10, y=150)
tk.Label(labelframe, text="", font=('Helvetica', 12), fg='red', textvariable=nsalText).place(x=100, y=150)
#Definig the lableframe for the convert button and setting up the Function (OK) to be called when the button is pressed.
tk.Button(labelframe, text="Cal", command=Ok, height=1, width=3).place(x=100, y=110)

e1 = tk.Entry(labelframe)
e1.place(x=80, y=80)

root.mainloop()
