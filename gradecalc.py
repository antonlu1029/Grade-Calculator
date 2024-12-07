#ask for input for amount of categories
#for each category, create something that has the grade type,
#percentage of grade, points earned, and possible points

import tkinter as tk
from tkinter import *
from tkinter import simpledialog

def calc_grade():
    sum = 0
    for i in range(typeNum):
        sum += (int(entryList[i][0].get()) * int(entryList[i][1].get()))/int(entryList[i][2].get())
    resultBox.delete(0, END)
    resultBox.insert(0, sum)

t = tk.Tk()
t.geometry("500x500")

typeNum = tk.simpledialog.askinteger("Test", "Enter the amount of grade categories:")

frame = Frame(t)
frame.pack(side = TOP)

frame2 = Frame(t)
frame2.pack(side = BOTTOM)

typeList = []
entryList = []

for i in range(typeNum):
    parameters = []
    typeList.append(Entry(frame, width = 15, textvariable = StringVar()))
    typeList[i].grid(row = i, column = 1)
    for j in range(3):
        parameters.append(Entry(frame, width = 5, textvariable = IntVar()))
        parameters[j].grid(row = i, column = j*2 + 3)
    Label(frame, text = "Grade Type:").grid(row = i, column = 0)
    Label(frame, text = "% of Grade:").grid(row = i, column = 2)
    Label(frame, text = "Points Earned:").grid(row = i, column = 4)
    Label(frame, text = "Points Possible:").grid(row = i, column = 6)
    entryList.append(parameters)
Button(frame, text = "Compute", command = calc_grade).grid(row = i+1, column = 0)

Label(frame2, text = "Grade (%): ").grid(row = 0, column = 0)
resultBox = Entry(frame2, textvariable = StringVar(value = str(0)))
resultBox.grid(row = 1, column = 0)

t.mainloop()
