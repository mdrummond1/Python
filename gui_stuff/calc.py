from tkinter import *
import parser

root = Tk()
root.title('Calculator')

#get user input and put it in text field
i = 0
def get_variable(num):
    global i
    display.insert(i, num)
    i += 1
   

#clearing display
def clear_all():
    global i
    display.delete(0, END)
    i = 0

#input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#backspace
def backspace():
    global i
    display.delete(i-1)
    i -= 1
    if i <  0:
        i = 0

    #or
    """ entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error") """

def get_operation(op):
    global i
    length = len(op)
    display.insert(i, op)
    i += length

#factorial
def fact(num):
    if num == 0:
        return 1
    if num < 0:
        print ("ERROR! must be a positive value.")
        return 0
    return num * fact(num - 1)

def get_fact():
    global i
    
    num = int(display.get())
    
    res = fact(num)
    
    clear_all()

    display.insert(0, res)

    i += len(str(res))



def calculate():
    global i
    string = display.get()
    
    try:
        a = parser.expr(string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    
    except Exception:
        clear_all()
        display.insert(0, "Error")
    
    i = len(str(result))


#adding buttons
"""
-------------
1   2   3   +   
4   5   6   -
7   8   9   *
    0       /
"""
Button(root, text="1", bg="lavender", command=lambda :get_variable(1)).grid(row=2, column=0)
Button(root, text="2", bg="lavender",  command=lambda :get_variable(2)).grid(row=2, column=1)
Button(root, text="3", bg="lavender",  command=lambda :get_variable(3)).grid(row=2, column=2)

Button(root, text="4", bg="lavender",  command=lambda :get_variable(4)).grid(row=3, column=0)
Button(root, text="5", bg="lavender",  command=lambda :get_variable(5)).grid(row=3, column=1)
Button(root, text="6", bg="lavender",  command=lambda :get_variable(6)).grid(row=3, column=2)

Button(root, text="7", bg="lavender",  command=lambda :get_variable(7)).grid(row=4, column=0)
Button(root, text="8", bg="lavender",  command=lambda :get_variable(8)).grid(row=4, column=1)
Button(root, text="9", bg="lavender",  command=lambda :get_variable(9)).grid(row=4, column=2)

Button(root, text="0", bg="lavender", command=lambda :get_variable(0)).grid(row=5, column=1
)

#Adding function buttons
Button(root, text="AC", bg="DodgerBlue2", command=lambda :clear_all()).grid(row=5, column=0)
Button(root, text="=", bg="DodgerBlue2", command=lambda :calculate()).grid(row=5, column=2)

Button(root, text="+", bg="gold",  command=lambda :get_operation("+")).grid(row=2, column=3)
Button(root, text="-", bg="gold",  command=lambda :get_operation("-")).grid(row=3, column=3)
Button(root, text="*", bg="gold",  command=lambda :get_operation("*")).grid(row=4, column=3)
Button(root, text="/", bg="gold",  command=lambda :get_operation("/")).grid(row=5, column=3)

#new operations
Button(root, text="pi", bg="gold",  command=lambda :get_operation("3.14")).grid(row=2, column=4)
Button(root, text="%", bg="gold",  command=lambda :get_operation("%")).grid(row=3, column=4)
Button(root, text="(", bg="gold",  command=lambda :get_operation("(")).grid(row=4, column=4)
Button(root, text="exp", bg="gold",  command=lambda :get_operation("**")).grid(row=5, column=4)

Button(root, text="<-", bg="gold",  command=lambda :backspace()).grid(row=2, column=5)
Button(root, text="x!", bg="gold",  command=lambda :get_fact()).grid(row=3, column=5)
Button(root, text=")", bg="gold",  command=lambda :get_operation(")")).grid(row=4, column=5)
Button(root, text="^2", bg="gold",  command=lambda :get_operation("**2")).grid(row=5, column=5)

root.mainloop()