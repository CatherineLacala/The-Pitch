#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 22:14:17 2026

@author: trey
"""
import sqlite3
import tags_implement
from datetime import datetime

#ID Markers fix this later 


class User: 
    #test this tmmr 
    def __init__(self, username, password):
        self.username = username
        self.password = password 
        
        #adding info to User class 
        with sqlite3.connect("users.db") as connect:
            cursor = connect.cursor()
            
            user_count = "SELECT COUNT(*) FROM Users;"
            
            cursor.execute(user_count)
            rows = cursor.fetchone()
            
            self.user_id = 1000 + rows[0]
            
            
            insert = "INSERT INTO Users Values (?, ?, ?)"
            cursor.execute(insert, [self.user_id, 
                                    self.username, 
                                    self.password])
    def get_username(self): 
        return self.username
    
        
    def store_script(self, title, genre, rating, movieOrTv, summery, script):
        with sqlite3.connect("tags.db") as connect:
            cursor = connect.cursor()
            insert = "INSERT INTO Tags VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            
                        
            post_count = "SELECT COUNT(*) FROM Tags;"
            
            cursor.execute(post_count)
            rows = cursor.fetchone()
            
            post_id = 1000 + rows[0]
            
            #make sure to fix the id incrementer 
            cursor.execute(insert, [post_id, 
                                    self.user_id, 
                                    self.username,
                                    datetime.today().strftime('%Y-%m-%d'), 
                                    title,
                                    genre,
                                    rating, 
                                    movieOrTv,
                                    summery, 
                                    script])
        

#TESTING
'''
connect = sqlite3.connect("tags.db")
cursor = connect.cursor()


u = User("test_user", "randompassword")


u.store_script("test_title", tags_implement.genre[0],tags_implement.movie_rating[0], tags_implement.movie_or_tv[0], "Welcome to SparkHacks", "Hello Sparkhacks!")

sql = "SELECT * From Tags" 

cursor.execute(sql)
all_rows = cursor.fetchall() # Fetches all rows into 'all_rows'


for row in all_rows:
    print(row)

connect.close() 

'''