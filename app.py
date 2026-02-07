import tkinter as tk

def clear_screen():
    # clearing screen
    for widget in root.winfo_children():
        widget.destroy()

def screenwriter_dashboard():
    clear_screen()
    tk.Label(root, text="What do you want to do?", font=("Arial", 18)).pack(pady=30)

    # 3 buttons
    tk.Button(root, text="Post Idea", width=25, command=lambda: print("Post Idea clicked")).pack(pady=10)
    tk.Button(root, text="Browse for Collaborators", width=25, command=lambda: print("Browse Collaborators clicked")).pack(pady=10)
    tk.Button(root, text="Browse Ideas", width=25, command=lambda: print("Browse Ideas clicked")).pack(pady=10)

def select_occupation():
    clear_screen()

    # new screen asing "Who are you?"
    tk.Label(root, text="Who are you?", font=("Arial", 18)).pack(pady=20)

    # defining the dropdown options
    job_variable = tk.StringVar(root)
    job_variable.set("Select a role")
    role_options = ["Screenwriter", "Producer", "Director"]

    # creating dropdown of role options
    job_dropdown = tk.OptionMenu(root, job_variable, *role_options)
    job_dropdown.pack(pady=10)

    def confirm_job():
        selected = job_variable.get()
        if selected == "Screenwriter":
            screenwriter_dashboard()
        else:
            print(f"Logic for {selected} not implemented yet")
    # confirming option
    confirm_button = tk.Button(root, text="Continue", command=confirm_job)
    confirm_button.pack(pady=20)

def create_account():
    username = user_txt.get()
    password = pass_txt.get()
    if username and password:
        print(f"Account created for: {username}")
        select_occupation()
    else:
        print("Please enter both username and password")

# Create the main window
root = tk.Tk()
root.title("The Pitch - Sign Up")
root.geometry("1500x900") # Set the window size

# Add a label widget
label = tk.Label(root, text="Welcome to The Pitch!")
label.pack(pady=20) # Add padding for better layout

#creating the username
tk.Label(root, text="Username").pack()
user_txt = tk.Entry(root) # making the input box
user_txt.pack(pady=5)

# creating password spot
tk.Label(root, text="Password:").pack()
pass_txt = tk.Entry(root, show="*") # "*" hides the characters
pass_txt.pack(pady=5)

# create account button
submit_account_button = tk.Button(root, text="Create Account", command=create_account)
submit_account_button.pack(pady=20)

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
