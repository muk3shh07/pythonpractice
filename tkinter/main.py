import tkinter as tk
def greet():
    label.config(text = "Namaste!Welcome to Nepal")
root =tk.Tk()

root.title("My first App")

root.geometry("300x200")

label = tk.Label(root, text="")

button = tk.Button(root, text="CLICK ME", command = greet)
button.pack(pady=40)

label.pack()

root.mainloop()