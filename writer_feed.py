#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 10:48:51 2026

@author: trey
"""
import tkinter as tk
from PIL import ImageTk, Image
import re
import sqlite3

toggle_menu_fm = None
toggle_btn = None

def toggle_menu(root):
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


def gather_info(): 
    
    with sqlite3.connect("tags.db") as connect:
      cursor = connect.cursor()
      
      sql = "SELECT Username, Title, Summery, Script FROM Tags ORDER BY Date_Posted asc;" #fix this      
      cursor.execute(sql)
      
      all_rows = cursor.fetchall()
      
      return all_rows 
  

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
                               command = lambda: toggle_menu(root))   
        
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
    
    
    rows = gather_info()
    
    feed_boxes(root, rows)



def feed_boxes(root, rows): 
    canvas = tk.Canvas(root, width=1000, height=800, bg="#f2d6c2")
    canvas.pack(pady=20)
    
    margin = 50
    gap = 25
    r_height = 120
    
    r_width = (1000 - 2 * margin)
    i = 0
    
    for row in rows[:4]: 
        y1 = margin + i * (r_height + gap)
        i += 1
        y2 = y1 + r_height
    
        canvas.create_rectangle(margin, y1, 
                                margin + r_width, y2, 
                                fill="white", 
                                outline="black", 
                                width = 3)
        
        
        def title_click(event, script_title):
            print(f"Opening script: {script_title}")
        
        tag_name = f"title_{row[0]}"
        #CHANGE THIS TO BUTTONNNNN 
        #Title
        canvas.create_text(margin+50, y1 + 20, text = row[1], 
                               fill = "#b51515",
                               font = ('Georgia', 20, 'underline'), tags=tag_name)
        
        canvas.tag_bind(tag_name, "<Button-1>", lambda e, t=row[1]: title_click(e, t))
        canvas.tag_bind(tag_name, "<Enter>", lambda e: canvas.config(cursor="hand2"))
        canvas.tag_bind(tag_name, "<Leave>", lambda e: canvas.config(cursor=""))

        canvas.create_text(margin+850, y1 + 20, text = row[0],
                               fill = "#b51515",
                               font = ('Georgia', 20))
        
        #Summary
        canvas.create_text(margin+100, y1 + 50, text = row[3], 
                               fill = "#b51515",
                               font = ('Georgia', 15)) 
        
        
        
    
# root = tk.Tk()
# root.title("The Pitch")
# root.geometry("1500x900") # Set the window size

# feed(root)

# # Start the Tkinter event loop
# if __name__ == "__main__":
#     root.mainloop()