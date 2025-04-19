import tkinter as tk
import tkinter.messagebox as messagebox
import random

# Global variable to keep track of the number of moves
move_count = 0

def move_cancel_button():
    global move_count
    move_count += 1
    if move_count >= 5:
        messagebox.showinfo("):", "میخوای از نمره دادن فرار کنی؟")
        move_count = 0  # Reset move_count to 0
    else:
        new_x = random.randint(10, 200)
        new_y = random.randint(10, 200)
        cancel_button.place(x=new_x, y=new_y)

# Function to display a second message box when the user presses "OK" and exit the app
def show_second_message_and_exit():
    messagebox.showinfo(":)", "آفرین آقای سبحانی")
    root.quit()  # Close the main window

# Create the main window
root = tk.Tk()
root.title("نمره بده ")

# Create and place a header label
header_label = tk.Label(root, text="اگه نمره ندی مرد نیستی", font=("Lalezar", 22))
header_label.pack()

# Create and place OK button with green background
ok_button = tk.Button(root, text="باشه نمره میدم", bg="green", fg="#fff", command=show_second_message_and_exit)
ok_button.pack()

# Create and place Cancel button with red background
cancel_button = tk.Button(root, text="نمره نمیدم", bg="red", fg="#fff")
cancel_button.pack()

# Bind the move_cancel_button function to the hover event
cancel_button.bind("<Enter>", lambda e: move_cancel_button())

# Run the Tkinter main loop
root.mainloop()
