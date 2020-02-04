from tkinter import *
import tkinter.messagebox
root = Tk()

#making a label
""" 
label1 = Label(root, text="Hello World!")
label1.pack() 
"""

#aligning items
#fg=foreground, bg=background
""" newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="Click Me!", fg="Red")
button2 = Button(otherframe, text="No! Click me!", fg="Blue")

button1.pack()
button2.pack() """

#using the grid
""" label1 = Label(root, text="First Name")
label2 = Label(root, text="Last Name")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1) """

#self adjusting widgets
""" label1 = Label(root, text="First", bg="Red", fg="White")
label1.pack(fill=X)

label2 = Label(root, text="Second", bg="Blue", fg="Green")
label2.pack(side=LEFT, fill=Y) """

#Handling buttons
""" def doThing():
    print("You clicked the button")
    label1 = Label(root, text="SURPRISE!", bg="Green", fg="White")
    label1.pack()
    
button1 = Button(root, text="Click Me!", command=doThing)
button1.pack() """

#Using classes with buttons
""" class MyButtons:
    def __init__(self, rootOne):
        frame = Frame(rootOne)
        frame.pack()

        self.printButton = Button(frame, text="Click da Button!", command=self.printMsg)
        self.printButton.pack()

        self.quitButton = Button(frame, text="Exit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMsg(self):
        print("The message")

b = MyButtons(root)

 """

 #built-in menus
"""def function1():
    print("Menu Item Clicked")

myMenu = Menu(root)
root.config(menu=myMenu)

submenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

menuEdit = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=menuEdit)
menuEdit.add_command(label="undo", command=function1)

#Toolbars
toolbar = Frame(root, bg="Pink")
insertBtn = Button(toolbar, text="Insert Files", command=function1)
insertBtn.pack(side=LEFT, padx=2, pady=3)

printBtn = Button(toolbar, text="Print", command=function1)
printBtn.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

#Make a status bar
status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X) """

#message box
""" tkinter.messagebox.showinfo("Title", "This is awesome!")

response = tkinter.messagebox.askquestion("question", "Do you like me?")

if response == 'yes':
    print("I like you too")
else:
    print(":(")
 """
#Creating graphics
canvas = Canvas(root, width="200", height="100")
canvas.pack()

newLine = canvas.create_line(0, 0, 100, 100)
otherLine = canvas.create_line(0, 0, 50, 100)
thirdLine = canvas.create_line(10, 10, 100, 100, fill="green")

root.mainloop()