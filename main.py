print("Hello SparkHacks")

import tkinter as tk
from PIL import ImageTk, Image

def select_occupation():
    # clearing screen
    for widget in root.winfo_children():
        widget.destroy()

    # new screen asing "Who are you?"
    tk.Label(root, text="Who are you?", font=("Arial", 18)).pack(pady=20)

    # defining the dropdown options
    job_variable = tk.StringVar(root)
    job_variable.set("Select a role")
    role_options = ["Screenwriter", "Producer", "Director"]

    # creating dropdown of role options
    job_dropdown = tk.OptionMenu(root, role_options, *role_options)
    job_dropdown.pack(pady=10)

    # confirming option
    confirm_button = tk.Button(root, text="Continue", command=lambda: print(f"Selected: {role_options.get()}"))
    confirm_button.pack(pady=20)

def create_account():
    username = user_txt.get()
    password = pass_txt.get()
    text = "Account created for: " + username;
    text_box.insert(tk.END, text)
    select_occupation()

# Create the main window
root = tk.Tk()
root.title("The Pitch - Sign Up")
root.geometry("1500x900") # Set the window size

# Add a label widget
label = tk.Label(root, text="Welcome to The Pitch!")
label.pack(pady=20) # Add padding for better layout

# Adding an image
logo_path = "The-Pitch-Logo.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((300,200), Image.Resampling.LANCZOS)

tk_logo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=tk_logo)

logo_label.pack(padx=10, pady=10)

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

# Create a text box
text_box = tk.Text(root, height=5, width=70)
text_box.pack(pady=10)

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
