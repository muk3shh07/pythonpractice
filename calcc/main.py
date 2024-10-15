import tkinter as tk
from tkinter import messagebox
# Function to calculate sum and show result
def find_sum():
    num1 = entry1.get()
    num2 = entry2.get()
    
    if num1.isdigit() and num2.isdigit():
        result = int(num1) + int(num2)
    messagebox.showinfo("Result", f"Sum: {result}")

# Create window
root = tk.Tk()
root.title("Addition App")
# Input fields
entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
# Button to find sum
tk.Button(root, text="Find Sum", command=find_sum).pack(pady=10)
# Start app
root.geometry("200x150")
root.mainloop()