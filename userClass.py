#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 22:14:17 2026

@author: trey
"""
import sqlite3
#import tags_implement
from datetime import datetime

#ID Markers fix this later 
global POST_ID = 2000
global USER_ID = 1000


class User: 
    #test this tmmr 
    def __init__(self,  username, password):
        self.user_id = USER_ID 
        self.username = username
        self.password = password 
        
        #adding info to User class 
        with sqlite3.connect("tags.db") as connect:
            cursor = connect.cursor()
            
            insert = "INSERT INTO Tags Values (?, ?, ?)"
            cursor.execute(insert, [self.user_id, 
                                    self.username, 
                                    self.password])
        USER_ID++
        

        
    def store_script(self, title, genre, rating, movieOrTv, script):
        with sqlite3.connect("tags.db") as connect:
            cursor = connect.cursor()
            insert = "INSERT INTO Tags VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        
            #make sure to fix the id incrementer 
            cursor.execute(insert, [POST_ID, 
                                    self.user_id, 
                                    self.username,
                                    datetime.today().strftime('%Y-%m-%d'), 
                                    title,
                                    genre,
                                    rating, 
                                    movieOrTv,
                                    script])
        POST_ID++
    
            
        

"""
TESTING
connect = sqlite3.connect("tags.db")
cursor = connect.cursor()

u = User("test_user", "randompassword")
u.store_script("test_title", tags_implement.genre[0],tags_implement.movie_rating[0], tags_implement.movie_or_tv[0], "Hello Sparkhacks!")

sql = "SELECT * FROM Tags"

cursor.execute(sql)
all_rows = cursor.fetchall() # Fetches all rows into 'all_rows'


for row in all_rows:
    print(row)

connect.close() """
