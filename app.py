import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import re
import userClass
import writer_feed

# storing global data
accounts = {}
connect = {}
user = ""

# Making lists to hold all the filters
filteringUser = []
filteringDate = []
filteringGenre = []
filteringRating = []
filteringType = []


def add_bg():
    # Adding a background image
    bg = Image.open("The-Pitch-BG.png")
    bg = bg.resize((1495,900), Image.Resampling.LANCZOS)


    root.bg_image = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(root, image=root.bg_image)
    #bg_label.image = bg_image
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


# Filter by user, date, genre, rating, and movie/show
def filterUser(filter_list):
    # Filtering by the user
    filteringUser = filter_list

def filterDate(filter_list):
    # Filtering by the date posted
    filteringDate = filter_list

def filterGenre(filter_list):
    # Filtering by the genre
    filteringGenre = filter_list

def filterRating(filter_list):
    # Filtering by the rating
    filteringRating = filter_list

def filterType(filter_list):
    # Filtering by the type (movie or tv show)
    filteringType = filter_list

def dashboard_layout(title, button_options):
    clear_screen()
    center = tk.Frame(root, bg="#f2d6c2")
    center.pack(expand=True)
    tk.Label(center, text=title, font=("Georgia", 22, "bold"), bg="#f2d6c2").pack(pady=30)


    # horizontal buttons
    column_frame = tk.Frame(center, bg="#f2d6c2")
    column_frame.pack(pady=20)

    def click_operation(choice):
        if choice == "Browse Ideas":
            clear_screen()
            writer_feed.feed(root)
        else:
            print(f"Clicked {choice}")

    for button_txt, description_txt in button_options:
        column = tk.Frame(column_frame, bg="#f2d6c2")
        column.pack(side="left", padx=30, anchor="n")

        # rounded button
        button = ctk.CTkButton(column, text=button_txt, width=200, height=50, corner_radius=25, fg_color="#3a3a3a", hover_color="#555555", command=lambda t=button_txt: click_operation(t))
        button.pack()

        # label
        tk.Label(column, text=description_txt, bg="#f2d6c2", fg="#555555", font=("Arial", 10), justify="center", wraplength=200).pack(pady=10)

    # back button
    back_button = ctk.CTkButton(center, text="← Back", width=80, corner_radius=15, fg_color="#d87455", hover_color="#b35f45", command=select_occupation)
    back_button.pack(pady=40)
    

def director_dashboard():
    # button descriptions
    button_options = [
        ("Search Scripts", "Find your next directorial masterpiece among \nthe latest community pitches."),
        ("Browse for Collaborators", "Assemble your crew and creative \ndepartment heads for your vision."),
        ("Search Producers", "Connect with the logistics and \nfinancing experts to get your film made.")
    ]
    dashboard_layout("Director Dashboard", button_options)


def producer_dashboard():
    # button descriptions
    button_options = [
        ("Search Scripts", "Discover scripts and concepts \nready for production."),
        ("Browse for Collaborators", "Connect with industry professionals \nto build your production team."),
        ("Search Directors", "Find the right creative vision and \nleadership for your next project.")
    ]
    dashboard_layout("Producer Dashboard", button_options)

def screenwriter_dashboard():
    # button descriptions
    button_options = [
        ("Pitch Idea", "Share your latest script or story \nconcept with the community."),
        ("Browse for Collaborators", "Find producers, directors, or screenwriters \nlooking for new talent or a partner."),
        ("Browse Ideas", "See what other writers are \nworking on for inspiration.")
    ]
    dashboard_layout("Screenwriter Dashboard", button_options)

def select_occupation():
    clear_screen()


    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    # new screen asing "Who are you?"
    tk.Label(center, text="Who are you?", font=("Georgia", 18), bg = "#f2d6c2").pack(pady=20)

    # defining the dropdown options
    job_variable = ctk.StringVar(value="Select a role")
    #job_variable.set("Select a role")
    role_options = ["Screenwriter", "Producer", "Director"]


    # creating dropdown of role options
    job_dropdown = ctk.CTkOptionMenu(center, variable=job_variable, values=role_options, width=200, height=40, corner_radius=20, fg_color="#3a3a3a", button_color="#2b2b2b", button_hover_color="#555555")
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
    confirm_button = ctk.CTkButton(center, text="Continue", corner_radius=20, fg_color="#d87455", hover_color="#b35f45", command=confirm_job)
    confirm_button.pack(pady=20)


def start_screen():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Welcome to The Pitch!", font=("Georgia", 20, "bold"), bg = "#f2d6c2").pack(pady=20)

    ctk.CTkButton(center, text="Sign In", width=200, corner_radius=20, fg_color="#d87455", hover_color="#b35f45", command=sign_in).pack(pady=10)
    ctk.CTkButton(center, text="Create Account", width=200, corner_radius=20, fg_color="#d87455", hover_color="#b35f45", command=create_account_screen).pack(pady=10)
    ctk.CTkButton(center, text="Continue as Guest", width=200, corner_radius=20, fg_color="#d87455", hover_color="#b35f45", command=continue_as_guest).pack(pady=10)

def create_account_screen():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Create Account", font=("Georgia", 22, "bold"), bg = "#f2d6c2").pack(pady=20)

    #tk.Label(center, text="Username").pack()
    user_txt = ctk.CTkEntry(center, placeholder_text="Username", width=250, height=40, corner_radius=20)
    user_txt.pack(pady=10)

    #tk.Label(center, text="Password").pack()
    pass_txt = ctk.CTkEntry(center, placeholder_text="Password", show="*", width=250, height=40, corner_radius=20)
    pass_txt.pack(pady=10)

    message = tk.Label(center, text="", fg="red", bg="#f2d6c2")
    message.pack(pady=5)


    def create_account():
        username = user_txt.get()
        #user = username;
        password = pass_txt.get()

        if username in accounts:
            message.config(text="Username already exists. Try different username.")
            return
        
        if not is_valid_password(password):
            message.config(text="Password must be 7+ characters, include uppercase, number, and special character.")
            return
    
        accounts[username] = password

        account = userClass.User(username, password)    # Creating a user object to add to the account to database
        connect[username] = account     # Saving the class object for the given username

        if not user_txt.get() or not pass_txt.get():
            message.config(text="Please fill in all fields.")
            return

        select_occupation()
    ctk.CTkButton(center, text="Create Account", width=250, height=45, corner_radius=20, fg_color="#3a3a3a", hover_color="#555555", command=create_account).pack(pady=15)
    ctk.CTkButton(center, text="← Back", width=80, corner_radius=15, fg_color="#d87455", hover_color="#b35f45", command=start_screen).pack()


def sign_in():
    clear_screen()

    # Creating a frame to center all the elements
    center = tk.Frame(root, bg = "#f2d6c2")
    center.pack(expand=True)

    tk.Label(center, text="Welcome Back! \nSign In", font=("Georgia", 22, "bold"), bg = "#f2d6c2").pack(pady=20)

    #tk.Label(center, text="Username").pack()
    user_txt = ctk.CTkEntry(center, placeholder_text="Username", width=250, height=40, corner_radius=20)
    user_txt.pack(pady=10)

    #tk.Label(center, text="Password").pack()
    pass_txt = ctk.CTkEntry(center, placeholder_text="Password", show="*", width=250, height=40, corner_radius=20)
    pass_txt.pack(pady=10)

    message = tk.Label(center, text="", fg="red", bg="#f2d6c2")
    message.pack(pady=5)


    def sign():
        username = user_txt.get()
        #user = username;
        password = pass_txt.get()


        if accounts.get(username) != password:
            message.config(text="Invalid username or password")
            return
        select_occupation()

    ctk.CTkButton(center, text="Sign In", width=250, height=45, corner_radius=20, fg_color="#3a3a3a", hover_color="#555555", command=sign).pack(pady=15)
    ctk.CTkButton(center, text="← Back", width=80, corner_radius=15, fg_color="#d87455", hover_color="#b35f45", command=start_screen).pack()
    # tk.Button(center, text="Back", command=start_screen).pack()

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



