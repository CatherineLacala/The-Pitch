#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 10:48:51 2026

@author: trey
"""
import tkinter as tk
from PIL import ImageTk, Image
import re

toggle_menu_fm = None
toggle_btn = None

def toggle_menu():
    global toggle_menu_fm
    
    if toggle_menu_fm is None: 
        toggle_menu_fm = tk.Frame(root, bg = "#b51515")
        window_height = root.winfo_height()
        toggle_menu_fm.place(x = 0, y = 100, height = window_height, width = 200)
        toggle_btn.config(text='X')
    else: 
        toggle_menu_fm.destroy()
        toggle_menu_fm = None
        toggle_btn.config(text='☰')


def feed(root):
    global toggle_btn
    
    header_frame = tk.Frame(root, bg = "#b51515", highlightbackground = "#f2d6c2", highlightthickness = 2)
    toggle_btn = tk.Button(header_frame, 
                               text = '☰', 
                               bg = "#b51515", 
                               fg = "#f2d6c2", 
                               font = ('Bold', 50), 
                               activebackground="#b51515",
                               activeforeground = "#b51515",
                               borderwidth=0,
                               highlightthickness=0,
                               command = toggle_menu)   
        
    toggle_btn.pack(padx= 20, side = tk.LEFT)
        
    title_lb = tk.Label(header_frame, text = 'What is the Sitch?', 
                               bg = "#b51515", 
                               fg = "#f2d6c2", 
                               font = ('Georgia', 50), 
                               bd = 0, 
                               activebackground="#f2d6c2",
                               activeforeground = '#f2d6c2')
        
    header_frame.pack(side = tk.TOP, fill = tk.X)
    header_frame.pack_propagate(False)
    header_frame.configure(height = 100)
    
    
    title_lb.pack(side = tk.LEFT)
    
# root = tk.Tk()
# root.title("The Pitch")
# root.geometry("1500x900") # Set the window size

# feed()

# Start the Tkinter event loop
#if __name__ == "__main__":
 #   root.mainloop()