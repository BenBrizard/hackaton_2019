#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:47:12 2019

@author: paulxing
"""

import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from scipy import asarray as ar,exp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(tk.Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        tk.Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Simulation of Aharonov–Bohm effect")



        # creating a menu instance
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)







class AB_Gui(tk.Frame):
    
    # Define settings upon initialization. 
    def __init__(self, master,PlotFrame):
        
        
        tk.Frame.__init__(self, master,PlotFrame) 
        
        self.master = master
        
        self.A_potential=0.00
        self.figure=Figure(figsize=(7, 3.5),dpi=85)
        self.create_widgets(PlotFrame)



    def create_widgets(self,PlotFrame):
         
         
        self.Label_PotentialVector = tk.Label(self.master,text='Enter the value of the potential vector: ')
        self.Label_PotentialVector.grid(row=0) 
        
        
        self.SetA_potential = tk.StringVar()
        self.Entry_BfieldValue = tk.Spinbox(self.master,from_=0.00, to=2.00,
                                           increment=0.01,textvariable=self.SetA_potential)
        self.Entry_BfieldValue.grid(row=0,column=1)
        
        
        
        self.label_space = tk.Label(self.master, text="T.m")
        self.label_space.grid(row=0,column=2)
        
        self.SubmitButton = tk.Button(self.master,text="Submit",
                                     command=self.button_function)
        self.SubmitButton.grid(row=0,column=3,columnspan=1,sticky=tk.E+tk.W)
        
        
        
        
        # a tk.DrawingArea
    
        self.canvas_Figure = FigureCanvasTkAgg(self.Figure, master=PlotFrame)
        self.canvas_Figure.draw()
        self.canvas_Figure.get_tk_widget().grid(row=0,columnspan=4,
                                              sticky=tk.E+tk.W+tk.N+tk.S)
        
        


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






        



class main_program(tk.Tk):
    
    
    
    # Define settings upon initialization.
    def __init__(self):
        
        # parameters send in the tkinter class is self only
        tk.Tk.__init__(self)
        
        self.window=Window(self)
        
        self.panedwindow = tk.PanedWindow(self, orient=tk.VERTICAL)
        
        self.Frame=tk.LabelFrame(self.panedwindow,text='',height=600,width=600)
        
        
        
        self.PlotFrame=tk.LabelFrame(self.panedwindow,
                                         text='Figure 1. Wave function',
                                         height=600, width=600)
        
        
        self.panedwindow.add(self.Frame)
        self.panedwindow.add(self.PlotFrame)
        
        self.FrameofGui=AB_Gui(self.Frame,self.PlotFrame)
        

        self.panedwindow.grid(row=0,column=0, columnspan = 5,sticky = tk.W+tk.E+tk.N)




#loading main program
app=main_program()

app.mainloop() 