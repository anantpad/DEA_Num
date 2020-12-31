import tkinter as tk

def closeApp():
    window.destroy()

window = tk.Tk()
window.title("My Play with Frames")
# window.geometry("300x300")
window.resizable(height="true", width="true")
window.minsize(height=600, width=600)

headerFrame = tk.Frame(window, borderwidth=5, bg="#9ae6c0", padx=240, pady=2)
contentFrame = tk.Frame(window, bg="#9ac0e6", borderwidth=5, padx=260, pady=2)
footerFrame = tk.Frame(window, bg="#ade69a", borderwidth=5, padx=270, pady=2)

headerFrame.grid(row=0,column=0)
contentFrame.grid(row=1,column=0)
footerFrame.grid(row=2,column=0)

MyHeading = tk.Label(headerFrame, text="My Personal Header", bg="#5adb23")
MyHeading.grid(row=0,column=0)

MyContent = tk.Label(contentFrame, text="My Content", bg="#2391db")
MyContent.grid(row=0,column=0)

MyFooter = tk.Label(footerFrame, text="My Foot", bg="#5adb23")
MyFooter.grid(row=0,column=0)

# headerFrame.pack()
# contentFrame.pack()
# footerFrame.pack()

window.mainloop()