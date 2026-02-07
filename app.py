import tkinter as tk
from PIL import ImageTk, Image
import re

# storing global data
accounts = {}

def add_bg():
    # Adding a background image
    bg = Image.open("The-Pitch-BG.png")
    bg = bg.resize((1495,900), Image.Resampling.LANCZOS)

    bg_image = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0)
    bg_label.lower()

def clear_screen():
    # clearing screen
    for widget in root.winfo_children():
        widget.destroy()

    add_bg()

def is_valid_password(password):
    if len(password) < 7:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def director_dashboard():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Director Dashboard", font=("Comic Sans MS", 30, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=30)

    # creating frame to hold the buttons horizontally on the screen
    button_frame = tk.Frame(center)
    button_frame.pack(pady=20)

    # buttons added to frame side="left"
    tk.Button(button_frame, text="Browse for Collaborators", width=25, command=lambda: print("Searching Collaborators")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Search Scripts", width=25, command=lambda: print("Searching Scripts")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Search Producers", width=25, command=lambda: print("Searching Directors")).pack(side="left", padx=10)


def producer_dashboard():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Producer Dashboard", font=("Comic Sans MS", 30, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=30)

    # creating frame to hold the buttons horizontally on the screen
    button_frame = tk.Frame(center)
    button_frame.pack(pady=20)

    # buttons added to frame side="left"
    tk.Button(button_frame, text="Browse for Collaborators", width=25, command=lambda: print("Searching Collaborators")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Search Scripts", width=25, command=lambda: print("Searching Scripts")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Search Directors", width=25, command=lambda: print("Searching Directors")).pack(side="left", padx=10)



def screenwriter_dashboard():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2",)
    center.pack(expand=True)

    tk.Label(center, text="Screenwriter Dashboard", font=("Comic Sans MS", 30, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=30)

    # creating frame to hold the buttons horizontally on the screen
    button_frame = tk.Frame(center)
    button_frame.pack(pady=20)

    # 3 buttons
    tk.Button(button_frame, text="Pitch Idea", width=25, command=lambda: print("Post Idea clicked")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Browse for Collaborators", width=25, command=lambda: print("Browse Collaborators clicked")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Browse Ideas", width=25, command=lambda: print("Browse Ideas clicked")).pack(side="left", padx=10)

def select_occupation():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    # new screen asing "Who are you?"
    tk.Label(center, text="Who are you?", font=("Comic Sans MS", 30, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=20)

    # defining the dropdown options
    job_variable = tk.StringVar(center)
    job_variable.set("Select a role")
    role_options = ["Screenwriter", "Producer", "Director"]

    # creating dropdown of role options
    job_dropdown = tk.OptionMenu(center, job_variable, *role_options)
    job_dropdown.pack(pady=10)

    def confirm_job():
        selected = job_variable.get()
        if selected == "Screenwriter":
            screenwriter_dashboard()
        elif selected == "Producer":
            producer_dashboard()
        elif selected == "Director":
            director_dashboard()
        else:
            print(f"Logic for {selected} not implemented yet")
    # confirming option
    confirm_button = tk.Button(center, text="Continue", command=confirm_job)
    confirm_button.pack(pady=20)

def start_screen():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Welcome to The Pitch!", font=("Comic Sans MS", 40, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=20)

    tk.Button(center, text="Sign In", width=25, command=sign_in).pack(pady=10)
    tk.Button(center, text="Create Account", width=25, command=create_account_screen).pack(pady=10)
    tk.Button(center, text="Continue as Guest", width=25, command=continue_as_guest).pack(pady=10)


def create_account_screen():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Create Account", font=("Comic Sans MS", 30, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=20)

    tk.Label(center, text="Username").pack()
    user_txt = tk.Entry(center)
    user_txt.pack(pady=5)

    tk.Label(center, text="Password").pack()
    pass_txt = tk.Entry(center, show="*")
    pass_txt.pack(pady=5)

    message = tk.Label(center, text="", fg="red")
    message.pack(pady=5)

    def create_account():
        username = user_txt.get()
        password = pass_txt.get()

        if username in accounts:
            message.config(text="Username already exists. Try different username.")
            return
        
        if not is_valid_password(password):
            message.config(text="Password must be 7+ characters, include uppercase, number, and special character.")
            return
        
        accounts[username] = password
        select_occupation()
    tk.Button(center, text="Create Account", command=create_account).pack(pady=15)
    tk.Button(center, text="Back", command=start_screen).pack()


def sign_in():
    clear_screen()
    
    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Sign In", font=("Comic Sans MS", 30, "bold"), bg = "#f2d6c2", fg = "#b51515").pack(pady=20)

    tk.Label(center, text="Username").pack()
    user_txt = tk.Entry(center)
    user_txt.pack(pady=5)

    tk.Label(center, text="Password").pack()
    pass_txt = tk.Entry(center, show="*")
    pass_txt.pack(pady=5)

    message = tk.Label(center, text="", fg="red")
    message.pack(pady=5)

    def sign():
        username = user_txt.get()
        password = pass_txt.get()

        if accounts.get(username) != password:
            message.config(text="Invalid username or password")
            return
        select_occupation()

    tk.Button(center, text="Sign In", command=sign).pack(pady=15)
    tk.Button(center, text="Back", command=start_screen).pack()

def continue_as_guest():
    select_occupation()

# Create the main window
root = tk.Tk()
root.title("The Pitch")
root.geometry("1500x900") # Set the window size

start_screen()


# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
