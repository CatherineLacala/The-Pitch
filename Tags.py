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
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY NOT NULL, 
    User TEXT NOT NULL,
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




