import customtkinter as tk
import customtkinter 
import string
import random
import pyperclip
from tkinter import messagebox

# Define a function to generate a random password
def generate_password():
    # Get the desired password length from the text box
    password_length = int(length_entry.get())


    # Define the characters to use in the password
    password_chars = string.ascii_letters
    if include_numbers.get():
        password_chars += string.digits
    if include_special_chars.get():
        password_chars += string.punctuation
 

    # Generate a password with the desired length
    password = ''.join(random.choice(password_chars) for i in range(password_length))

    # Update the label to display the generated password
    password_label.configure(text=password)

# Define a function to copy the password to the clipboard
def copy_password():
    password = password_label.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", "The password has been copied to the clipboard.")
    

# Create the main window
root = tk.CTk()
root.title("Password Generator")
root.geometry("400x320")

customtkinter.set_default_color_theme("blue") 

# Create a label for the password length text box
length_label = tk.CTkLabel(root, text="Password length:", font=("Arial", 14))
length_label.pack()

# Create a text box for the password length
length_entry = tk.CTkEntry(root, font=("Arial", 14))
length_entry.pack(pady=10)

# Create a check box for including numbers in the password
include_numbers = tk.BooleanVar()
number_check = tk.CTkCheckBox(root, text="Include numbers", font=("Arial", 14), variable=include_numbers)
number_check.pack(pady=10)

# Create a check box for including special characters in the password
include_special_chars = tk.BooleanVar()
special_check = tk.CTkCheckBox(root, text="Include special characters", font=("Arial", 14), variable=include_special_chars)
special_check.pack(pady=10)

# Create a button to generate a new password
generate_button = tk.CTkButton(root, text="Generate Password", font=("Arial", 14), command=generate_password)
generate_button.pack(pady=10)

# Create a label to display the generated password
password_label = tk.CTkLabel(root, text="", font=("Arial", 16))
password_label.pack(pady=10)

# Create a button to copy the password to the clipboard and make it greyed out if there is no password
copy_button = tk.CTkButton(root, text="Copy Password", font=("Arial", 14), command=copy_password)

copy_button.pack(pady=10)

# Run the main event loop
root.mainloop()
