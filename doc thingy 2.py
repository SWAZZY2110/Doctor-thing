#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:31:24 2022

@author: priyankadas
"""

from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("Are you ok?")
root.geometry("400x400")
root.configure(bg="gold")


q1 = Label(root, text = "Do you have a fever?")
q1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
q1var = StringVar(value = "0")
q1r1 = Radiobutton(root, text = "Yes", variable = q1var, value = "yes")
q1r1.place(relx = 0.5, rely = 0.25, anchor = CENTER)
q1r2 = Radiobutton(root, text = "No", variable = q1var, value = "no")
q1r2.place(relx = 0.5, rely = 0.3, anchor = CENTER)

q2 = Label(root, text = "Do you have a runny-nose?")
q2.place(relx = 0.5, rely = 0.35, anchor = CENTER)
q2var = StringVar(value = "0")
q2r1 = Radiobutton(root, text = "Yes", variable = q2var, value = "yes")
q2r1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
q2r2 = Radiobutton(root, text = "No", variable = q2var, value = "no")
q2r2.place(relx = 0.5, rely = 0.45, anchor = CENTER)

q3 = Label(root, text = "Do you have loss of breath?")
q3.place(relx = 0.5, rely = 0.5, anchor = CENTER)
q3var = StringVar(value = "0")
q3r1 = Radiobutton(root, text = "Yes", variable = q3var, value = "yes")
q3r1.place(relx = 0.5, rely = 0.55, anchor = CENTER)
q3r2 = Radiobutton(root, text = "No", variable = q3var, value = "no")
q3r2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

q4 = Label(root, text = "Do you have a headaches?")
q4.place(relx = 0.5, rely = 0.65, anchor = CENTER)
q4var = StringVar(value = "0")
q4r1 = Radiobutton(root, text = "Yes", variable = q4var, value = "yes")
q4r1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
q4r2 = Radiobutton(root, text = "No", variable = q4var, value = "no")
q4r2.place(relx = 0.5, rely = 0.75, anchor = CENTER)

q5 = Label(root, text = "Do you have fatigue?")
q5.place(relx = 0.5, rely = 0.8, anchor = CENTER)
q5var = StringVar(value = "0")
q5r1 = Radiobutton(root, text = "Yes", variable = q5var, value = "yes")
q5r1.place(relx = 0.5, rely = 0.85, anchor = CENTER)
q5r2 = Radiobutton(root, text = "No", variable = q5var, value = "no")
q5r2.place(relx = 0.5, rely = 0.9, anchor = CENTER)

total = Label(root)
total.place(relx = 0.75, rely = 0.9, anchor = CENTER)
def check():
    score = 0
    if(q1var.get() == "yes"):
        score = score+20
    if(q2var.get() == "yes"):
        score = score+20
    if(q3var.get() == "yes"):
        score = score+20
    if(q4var.get() == "yes"):
        score = score+20
    if(q5var.get() == "yes"):
        score = score+20
        
    if(score <20):
        message.showinfo("Report- There is no problems dectected, you are free to go.") 
    elif(score == 20):
        message.showinfo("Report- Single issue decteted, no urgent care needed how ever take care.")
    elif(score >20 and score <=40):
        message.showinfo("Report- Slight problems have been diagnosed, doctor is not required.")
    elif(score >40 and score <=60):
        message.showinfo("Report- Multiple issue's diagnosed, doctors care is reccommended although not required.")
    elif(score >60 and score <=80):
        message.showinfo("Report- Multiple issue's diagnosed, doctors care is nessecery.")
    else:
        message.showinfo("Report- Several issue's diagnosed, doctor's care is heavily recommended.")
        

btn = Button(root, text = "Helth Check", command = check)
btn.place(relx = 0.25, rely = 0.9, anchor = CENTER)

root.mainloop()

#0.2, 0.3, 0.35 - 0.5, 0.6, 0.65- 0.8, 0.9, 0.95