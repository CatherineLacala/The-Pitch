What is the Pitch? 
  The Pitch it meant to be an application to sort and filter scripts from screenwriters. This app has no established algorithm, 
and is meant to give every script a fair shot at getting seen. 

The Pitch allows screenwriters, producers, and directors to post scripts, discover new pieces of work, and
 collaborate with others. Users can create an account, log into an existing account, or browse as a guest. 
 After choosing their role (screenwriter, producer, or director), they have the option to explore. 
 Screenwriters can pitch a script idea, browse for collaborators, and browse for ideas. 
 Producers can search for scripts, browse for collaborators, and browse for directors. 
 Finally, directors can search for scripts, browse for collaborators, and browse for producers. 

We used Python, Tkinter, and SQL to create our app.

To run the application, run python app.py.

First you must install Pillow and CTkinter using pip.
  pip install Pillow
  pip install customtkinter

Overview of code:
  We built the majority of this application in app.py using definitions, if statements, classes, and global variables. Then we created databases for the users and posts. The program starts with prompting the user to create an account, sign in, or continue as guest. Then, the user selects if they are a screenwriter, director, or producer. After that, the user gets 3 options under their certain role. Currently, only one of the screenwriter options is implemented and working. The working option is browse ideas, where the user can filter by genre, rating, and type (movie or tv show). Upon finalizing their filters, the user is able to see the scripts that correlate to those tags. 
