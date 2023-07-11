import tkinter as tk
from tkinter import font

def check_palindrome():
    word = entry.get()  # Get the word entered in the entry field
    reversed_word = word[::-1]
    if word.lower() == reversed_word.lower():
        result.config(text="It is a palindrome.")
    else:
        result.config(text="It is not a palindrome.")

# Function to handle button event
def get_input():
    text = entry.get()  # Get the value entered in the entry field
    print("Entered text:", text)

# Creating window
window = tk.Tk()

# Create the entry field
entry = tk.Entry(window)

# Position the entry field in the window
entry.pack()

# Create the button
button = tk.Button(window, text="Check", command=check_palindrome)

# Create the label to display the result
result = tk.Label(window)
result.pack()

# Position the button in the window
button.pack()
button.place(x=220, y=180)
entry.place(x=180, y=150)

# Creating font instances in the window
large_font = font.Font(size=15)
medium_font = font.Font(size=13)
small_font = font.Font(size=12)

# Creating labels for fonts
large_label = tk.Label(window, text="Hello! Welcome!", font=large_font)
medium_label = tk.Label(window, text="Now let's check if the word is a palindrome.", font=medium_font)
small_label = tk.Label(window, text="Enter a word or text:")

# Displaying the labels in the window
large_label.pack()
medium_label.pack()
small_label.pack()

# Set window attributes
window.title("Window Test")
window.geometry("500x500")
window.mainloop()