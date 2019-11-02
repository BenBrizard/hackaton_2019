#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:49:59 2019

@author: paulxing
"""
import numpy as np
import tkinter as tk
from tkinter import messagebox


class AB_Gui(tk.Frame):
    
    # Define settings upon initialization. 
    def __init__(self, master):
        
        
        tk.Frame.__init__(self, master) 
        
        self.master = master
        
        self.A_potential=0.00
        self.create_widgets()



    def create_widgets(self):
         
         
        self.Label_PotentialVector = tk.Label(self.master,text='Enter the value of the potential vector: ')
        self.Label_PotentialVector.grid(row=0) 
        
        
        self.SetA_potential = tk.StringVar()
        self.Entry_BfieldValue = tk.Spinbox(self.master,from_=0.00, to=2.00,
                                           increment=0.01,textvariable=self.SetA_potential)
        self.Entry_BfieldValue.grid(row=0,column=1)
        
        
        
        
        self.SubmitButton = tk.Button(self.master,text="Submit",
                                     command=self.button_function)
        self.SubmitButton.grid(row=0,column=2,columnspan=2,sticky=tk.E+tk.W)
        
        self.label_space = tk.Label(self.master, text="T.m")
        self.label_space.grid(row=0,column=4)


    def button_function(self):
        
        try:
             self.A_potential=float(self.SetA_potential.get())
             message_rate="Your potential vector amplitude is "+self.SetA_potential.get()+" (t.m)."
             messagebox.showinfo("Message", message_rate)
             # the exception avoid the programm to crash when the user makes a mistake
        except ValueError:
            messagebox.showerror("Message", "ValueError. Please try again.")
            pass
        except IndexError:
            messagebox.showerror("Message", "IndexError. Please try again.")
            pass
        except TypeError:
            messagebox.showerror("Message", "TypeError. Please try again.")
            pass
        except NameError:
            messagebox.showerror("Message", "NameError. Please try again.")
            pass 
