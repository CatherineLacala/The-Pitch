#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 19:28:48 2026

@author: Breanna Brown 
"""
import sqlite3


dbConnect = sqlite3.connect("tags.db")

cursor = dbConnect.cursor()


#info gathered when user posts 
user_posts = """
CREATE TABLE IF NOT EXISTS Tags (
    Post_ID INTEGER PRIMARY KEY NOT NULL, 
    User_ID INTEGER NOT NULL,
    Username TEXT NOT NULL,
    Date_Posted DATE,
    Title TEXT NOT NULL,
    Genre TEXT NOT NULL,
    Rating TEXT NOT NULL,
    Movie_or_TV TEXT NOT NULL, 
    Script TEXT NOT NULL
);
"""

cursor.execute(user_posts)

dbConnect.commit()
dbConnect.close()

dbConnect = sqlite3.connect("users.db")
cursor = dbConnect.cursor()

#user info
user_data = """
    CREATE TABLE IF NOT EXISTS Users (
        User_ID INTEGER PRIMARY KEY NOT NULL, 
        Username TEXT NOT NULL,
        Password TEXT NOT NULL
        
    );
"""

cursor.execute(user_data)

dbConnect.commit()
dbConnect.close()





