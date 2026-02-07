import tkinter as tk

def create_account():
    username = user_txt.get()
    password = pass_txt.get()
    print(f"Account created for: {username}")

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
