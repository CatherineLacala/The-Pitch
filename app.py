import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Screen App")
root.geometry("1500x900") # Set the window size

# Add a label widget
label = tk.Label(root, text="Welcome to The Pitch!")
label.pack(pady=20) # Add padding for better layout

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
