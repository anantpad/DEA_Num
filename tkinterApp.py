import tkinter as tk
from DEA import *


def close_app():
    window.destroy()

def reset():
    lname_entry.delete(first=0,last=20)
    deaValue.delete(first=0, last=20)
    lname_entry.focus()


def run_app():
    print("getting user input on Last Name")
    user_lastName = lname_entry.get()
    value.set(generateDEANum(user_lastName))


# I will need the functions because we need to use them with the bind method in the Entry boxes
def capslname1(event):
    lname1.set(lname1.get().upper())


# window
window = tk.Tk()
window.title("DEA Number")
# window.minsize(width=250, height=200)
# window.geometry("600x600")
window.resizable(width="true", height="true")

# widgets Frames: our app will be divided into three frames stacked on top of each other. The top frame will be used
# to place our header, while the bottom will display our app buttons. The frame in the middle will consist of two
# other frames (yes, you can place a widget inside another widget!) When we create the frames, we need to tell
# Tkinter which window they belong to, and we define that with passing the window variable (our main window) as the
# master for the frame. I’ve added some arguments like border width and pady (padding y-axis) to make it look nicer.
# When we create the frames, we need to tell Tkinter which window they belong to, and we define that with passing the
# window variable (our main window) as the master for the frame. The key point here is that the argument master is
# used in every widget and that is what defines where the widget is placed
frame_header = tk.Frame(window)
frame_content = tk.Frame(window)
frame_footer = tk.Frame(window)

# Grid: I will use Grid as one way to define the layout of the app. If you’re feeling adventurous feel free to try
# Place, which lets you set the position with specific x,y coordinates of the screen. In my opinion, Grid is the
# easiest to understand and to work with so we’ll be using that and Pack. I used the grid method to place them in the
# app. You may have already noticed that the header is on top(row 0 and column 0), the center is… well in the center(
# 1, 0), and the bottom frame is below the center # frame(2, 0). the frames would only show up if they had some sort
# of elements there
frame_header.grid(row=0, column=0, pady=10)
frame_content.grid(row=1, column=0, pady=5, padx=5)
frame_footer.grid(row=2, column=0, pady=5)

# header
# Labels: simply put, they’re textboxes. We’ll use it in the header and next to the entry boxes.
header = tk.Label(frame_header, text="Generate DEA number", bg="#582c83", fg="white", relief="raised", font=("calibri", "14"), anchor="n",
                  justify="l")
header.grid(row=0, column=0, ipadx=5, ipady=2)

# Content
# The frame in the middle will consist of two other frames (yes, you can place a widget inside another widget!)
# Let's add two more frames inside the center frame, frame_main1 and frame_main2
frame_main1 = tk.Frame(frame_content)
frame_main2 = tk.Frame(frame_content)

# let's also add the labels for those frames
# We tell Tkinter the labels belong to frame 1 and 2, and what text they will display
lname = tk.Label(frame_main1, text="Last Name:", font=("calibri", "11"), width=12, pady=2, anchor="e")
deaNum = tk.Label(frame_main2, text="Mock DEA Num:", font=("calibri", "11"), width=12, pady=2, anchor="e")
# The point of having a GUI is to let the user interact more fluently with the program, so we need to decide what we
# want the user to give us as inputs. we are expecting strings from the user
lname1 = tk.StringVar()
value = tk.StringVar()
# value.set("Output")

# Entries: it’s the widget that lets the user write some kind of input like the cities and the dates.
# I want to have an entry box for each one of the labels there
lname_entry = tk.Entry(frame_main1, textvariable=lname1)
# What .bind() does is to wait for an event to happen in the widget and run a sequence/function. In this case,
# the widget is the entry box, the event is a key release, and the function will transform the letters into upper case.
lname_entry.bind("<KeyRelease>", capslname1)
deaValue = tk.Entry(frame_main2, textvariable=value)

# Pack: it is also a layout manager and it’s really easy to understand…
# every time you use .pack() it will stack that widget under the previously packed one.
frame_main1.pack()
frame_main2.pack()
lname.pack(side="left")
lname_entry.pack(side="left")
deaNum.pack(side="left")
deaValue.pack(side="left")

# Footer Buttons: there is an argument called command inside the button widgets that tells the button what function
# to run when it is pressed. We will also have two buttons, one to run the bot, and another to exit the app The
# Button widget is easily mapped with a function in the argument “command=”. Notice how I direct one to the run_app
# function and the other to close_app. Oh, and the master for these buttons is the bottom_frame.
button_run = tk.Button(frame_footer, text="Generate DEA number", bg="green", fg="white", command=run_app, font=("calibri", "11"))
button_run.grid(column=0, row=0, padx=5)

button_reset = tk.Button(frame_footer, text="Reset", command=reset, bg="brown", fg="white", font=("calibri", "11"))
button_reset.grid(column=1, row=0, padx=5)

button_close = tk.Button(frame_footer, text="Close", command=close_app, bg="red", fg="white", font=("calibri", "11"))
button_close.grid(column=2, row=0, padx=5)

lname_entry.focus()
window.mainloop()