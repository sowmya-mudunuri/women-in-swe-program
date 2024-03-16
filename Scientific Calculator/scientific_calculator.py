import tkinter as tk
from tkinter import *
import math 
from math import *
import PIL
from PIL import ImageTk, Image
    
# Button parameters
btn_params = {'padx': 16, 'pady': 1, 'bd': 4, 'fg': 'white', 'bg': '#0A0A0A', 'font': ('arial', 18),
              'width': 2, 'height': 2, 'relief': 'raised', 'activebackground': 'black'}
 
# Custom functions
def log10(arg):
    return math.log(arg,10)
def ln(arg):
    return math.log(arg)

# For result in degrees and radians 
def sine(arg):
    return sin(arg * convert_constant) 
def cosine(arg):
    return cos(arg * convert_constant)
def tangent(arg):
    return tan(arg * convert_constant) 

def sininv(arg):
    return inverse_convert_constant * (asin(arg))
def cosinv(arg):
    return inverse_convert_constant * (acos(arg))
def taninv(arg):
    return inverse_convert_constant * (atan(arg))

class Calculator:
    def __init__(self, master):
        # Stores expression that will be displayed on screen
        self.expression = ""

        # Stores data in memory
        self.recall = ""

        # For ans 
        self.sum_up = ""

        # Creates string for text input
        self.text_input = tk.StringVar()

        # Assigns instance to master
        self.master = master

        # Sets frame showing inputs and title
        top_frame = tk.Frame(master, width=650, height=10,
                             bd=10, relief='flat', bg='gray')
        top_frame.pack(side=tk.TOP)

        # Sets frame showing all buttons
        bottom_frame = tk.Frame(
            master, width=650, height=470, bd=2, relief='flat', bg='black')
        bottom_frame.pack(side=tk.BOTTOM)
       
        # Calculator Display
        # Top frame - input and output interface
        txt_display = tk.Entry(top_frame, font=('arial', 36), relief='flat', bg='black', fg='white', textvariable=self.text_input, width=60, bd=12, justify='right')
        txt_display.pack()
 
        # Row 0
        # Left bracket (
        self.btn_left_brack = tk.Button(bottom_frame, **btn_params, text="(", command=lambda: self.btn_click('('))
        self.btn_left_brack.configure(bg='#222f3e')
        self.btn_left_brack.grid(row=0, column=0)

        # Right bracket )
        self.btn_right_brack = tk.Button(bottom_frame, **btn_params, text=")", command=lambda: self.btn_click(')'))
        self.btn_right_brack.configure(bg='#222f3e')
        self.btn_right_brack.grid(row=0, column=1)

        # e power 
        self.btn_exp = tk.Button(bottom_frame, **btn_params, text="exp", command=lambda: self.btn_click('exp('))
        self.btn_exp.configure(bg='#222f3e')
        self.btn_exp.grid(row=0, column=2)

        # pi
        self.btn_pi = tk.Button(bottom_frame, **btn_params, text="π", command=lambda: self.btn_click('pi'))
        self.btn_pi.configure(bg='#222f3e')
        self.btn_pi.grid(row=0, column=3)

        # Square root 
        self.btn_sqrt = tk.Button(bottom_frame, **btn_params, text="√", command=lambda: self.btn_click('sqrt('))
        self.btn_sqrt.configure(bg='#222f3e')
        self.btn_sqrt.grid(row=0, column=4)

        # All clear button - clears self.expression
        self.btn_clear = tk.Button(bottom_frame, **btn_params, text="AC", command=self.btn_clear_all)
        self.btn_clear.configure(bg='#eb2f06', fg='black')
        self.btn_clear.grid(row=0, column=5)

        # Clear Entry button - deletes last string input
        self.btn_del = tk.Button(bottom_frame, **btn_params, text="C", command=self.btn_clear1)
        self.btn_del.configure(bg='#e55039', fg='black')
        self.btn_del.grid(row=0, column=6)

        # Inputs a negative sign to the next entry
        self.btn_change_sign = tk.Button(bottom_frame, **btn_params, text="+/-", command=self.change_signs)
        self.btn_change_sign.configure(bg='#F79F1F', fg='black', activebackground='#F79F1F')
        self.btn_change_sign.grid(row=0, column=7)

        # Division
        self.btn_div = tk.Button(bottom_frame, **btn_params, text="/", command=lambda: self.btn_click('/'))
        self.btn_div.configure(bg='#F79F1F', fg='black', activebackground='#F79F1F')
        self.btn_div.grid(row=0, column=8)
 
        # Row 1
        # Changes trig function outputs to degrees
        self.btn_Deg = tk.Button(bottom_frame, **btn_params, text="Deg", command=self.convert_deg)
        self.btn_Deg.configure(bg='#222f3e')
        self.btn_Deg.grid(row=1, column=0)

        # Changes trig function outputs to default back to radians
        self.btn_Rad = tk.Button(bottom_frame, **btn_params, text="Rad", command=self.convert_rad)
        self.btn_Rad.configure(bg='#222f3e')
        self.btn_Rad.grid(row=1, column=1)

        # Cube of a value
        self.cube = tk.Button(bottom_frame, **btn_params, text=u"x\u00B3", command=lambda: self.btn_click('**3'))
        self.cube.configure(bg='#222f3e')
        self.cube.grid(row=1, column=2)

        # Absolute value or mod
        self.btn_abs = tk.Button(bottom_frame, **btn_params, text="abs", command=lambda: self.btn_click('abs' + '('))
        self.btn_abs.configure(bg='#222f3e')
        self.btn_abs.grid(row=1, column=3)

        # 'Memory Clear' button. Wipes self.recall to an empty string
        self.btn_MC = tk.Button(bottom_frame, **btn_params, text="MC", command=self.memory_clear)
        self.btn_MC.configure(bg='#222f3e')
        self.btn_MC.grid(row=1, column=4)

        # Buttons 7-9
        self.btn_7 = tk.Button(bottom_frame, **btn_params, text="7", command=lambda: self.btn_click(7))
        self.btn_7.configure(bg='#576574')
        self.btn_7.grid(row=1, column=5)
        
        self.btn_8 = tk.Button(bottom_frame, **btn_params, text="8", command=lambda: self.btn_click(8))
        self.btn_8.configure(bg='#576574')
        self.btn_8.grid(row=1, column=6)
    
        self.btn_9 = tk.Button(bottom_frame, **btn_params, text="9", command=lambda: self.btn_click(9))
        self.btn_9.configure(bg='#576574')
        self.btn_9.grid(row=1, column=7)

        # Multiplication
        self.btn_mult = tk.Button(bottom_frame, **btn_params, text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.configure(bg='#F79F1F', fg='black', activebackground='#F79F1F')
        self.btn_mult.grid(row=1, column=8)
 
        # Row 2
        # Sin function
        self.btn_sin = tk.Button(bottom_frame, **btn_params, text="sin", command=lambda: self.btn_click('sine('))
        self.btn_sin.configure(bg='#222f3e')
        self.btn_sin.grid(row=2, column=0)

        # Cos function
        self.btn_cos = tk.Button(bottom_frame, **btn_params, text="cos", command=lambda: self.btn_click('cosine('))
        self.btn_cos.configure(bg='#222f3e')
        self.btn_cos.grid(row=2, column=1)

        # Tan function
        self.btn_tan = tk.Button(bottom_frame, **btn_params, text="tan", command=lambda: self.btn_click('tangent('))
        self.btn_tan.configure(bg='#222f3e')
        self.btn_tan.grid(row=2, column=2)

        # Natural logarithm (base e)
        self.btn_log = tk.Button(bottom_frame, **btn_params, text="ln", command=lambda: self.btn_click('ln('))
        self.btn_log.configure(bg='#222f3e')
        self.btn_log.grid(row=2, column=3)

        # Displays what is in self.recall
        self.btn_MR = tk.Button(bottom_frame, **btn_params, text="MR", command=self.memory_recall)
        self.btn_MR.configure(bg='#222f3e')
        self.btn_MR.grid(row=2, column=4)

        # Buttons 4 - 6
        self.btn_4 = tk.Button(bottom_frame, **btn_params, text="4", command=lambda: self.btn_click(4))
        self.btn_4.configure(bg='#576574')
        self.btn_4.grid(row=2, column=5)
        
        self.btn_5 = tk.Button(bottom_frame, **btn_params, text="5", command=lambda: self.btn_click(5))
        self.btn_5.configure(bg='#576574')
        self.btn_5.grid(row=2, column=6)
    
        self.btn_6 = tk.Button(bottom_frame, **btn_params, text="6", command=lambda: self.btn_click(6))
        self.btn_6.configure(bg='#576574')
        self.btn_6.grid(row=2, column=7)

        # Subtraction
        self.btnSub = tk.Button(bottom_frame, **btn_params, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.configure(bg='#F79F1F', fg='black', activebackground='#F79F1F')
        self.btnSub.grid(row=2, column=8)
 
        # Row 3
        # Sin inverse 
        self.btn_sin_inverse = tk.Button(bottom_frame, **btn_params, text=u"sin\u207B\u00B9", command=lambda: self.btn_click('sininv('))
        self.btn_sin_inverse.configure(bg='#222f3e')
        self.btn_sin_inverse.grid(row=3, column=0)

        # Cos inverse 
        self.btn_cos_inverse = tk.Button(bottom_frame, **btn_params, text=u"cos\u207B\u00B9", command=lambda: self.btn_click('cosinv('))
        self.btn_cos_inverse.configure(bg='#222f3e')
        self.btn_cos_inverse.grid(row=3, column=1)

        # Tan inverse 
        self.btn_tan_inverse = tk.Button(bottom_frame, **btn_params, text=u"tan\u207B\u00B9", command=lambda: self.btn_click('taninv('))
        self.btn_tan_inverse.configure(bg='#222f3e')
        self.btn_tan_inverse.grid(row=3, column=2)

        # Log base 10
        self.btn_ln = tk.Button(bottom_frame, **btn_params, text="log", command=lambda: self.btn_click('log10('))
        self.btn_ln.configure(bg='#222f3e')
        self.btn_ln.grid(row=3, column=3)

        # Adds current self.expression to self.recall string
        self.btn_M_plus = tk.Button(bottom_frame, **btn_params, text="M+", command=self.memory_add)
        self.btn_M_plus.configure(bg='#222f3e')
        self.btn_M_plus.grid(row=3, column=4)

        # Buttons 1-3
        self.btn_1 = tk.Button(bottom_frame, **btn_params, text="1", command=lambda: self.btn_click(1))
        self.btn_1.configure(bg='#576574')
        self.btn_1.grid(row=3, column=5)
        
        self.btn_2 = tk.Button(bottom_frame, **btn_params, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure(bg='#576574')
        self.btn_2.grid(row=3, column=6)
        
        self.btn_3 = tk.Button(bottom_frame, **btn_params, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure(bg='#576574')
        self.btn_3.grid(row=3, column=7)

        # Addition
        self.btn_add = tk.Button(bottom_frame, **btn_params, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.configure(bg='#F79F1F', fg='black', activebackground='#F79F1F')
        self.btn_add.grid(row=3, column=8)
 
        # Row 4
        # Factorial function
        self.btn_fact = tk.Button(bottom_frame, **btn_params, text="n!", command=lambda: self.btn_click('factorial('))
        self.btn_fact.configure(bg='#222f3e')
        self.btn_fact.grid(row=4, column=0)

        # Square
        self.btn_sqr = tk.Button(bottom_frame, **btn_params, text=u"x\u00B2", command=lambda: self.btn_click('**2'))
        self.btn_sqr.configure(bg='#222f3e')
        self.btn_sqr.grid(row=4, column=1)

        # Power
        self.btn_power = tk.Button(bottom_frame, **btn_params, text="x\u02b8", command=lambda: self.btn_click('**'))
        self.btn_power.configure(bg='#222f3e')
        self.btn_power.grid(row=4, column=2)

        # Stores previous expression as an answer value
        self.btn_ans = tk.Button(bottom_frame, **btn_params, text="ans", command=self.answer)
        self.btn_ans.configure(bg='#222f3e')
        self.btn_ans.grid(row=4, column=3)
        
        # Comma to allow more than one parameter
        self.btn_comma = tk.Button(bottom_frame, **btn_params, text=",", command=lambda: self.btn_click(','))
        self.btn_comma.configure(bg='#222f3e')
        self.btn_comma.grid(row=4, column=4)

        # 0 button
        self.btn_0 = tk.Button(bottom_frame, **btn_params, text="0", command=lambda: self.btn_click(0))
        self.btn_0.configure(bg='#576574', width=7, bd=5)
        self.btn_0.grid(row=4, column=5, columnspan=2)

        # Equal to button
        self.btn_eq = tk.Button(bottom_frame, **btn_params, text="=", command=self.btn_equal)
        self.btn_eq.configure(bg='#A3CB38', fg='black', activebackground='#A3CB38')
        self.btn_eq.grid(row=4, column=7)

        # Decimal
        self.btn_dec = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.configure(bg='#006266', activebackground='#006266')
        self.btn_dec.grid(row=4, column=8)
 
    # Functions
    # Allows button you click to be put into self.expression
 
    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)
 
    # Clears last item in string
 
    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)
 
    # Adds in a negative sign
 
    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)
 
    # Clears memory_recall
 
    def memory_clear(self):
        self.recall = ""
 
    # Adds whatever is on the screen to self.recall
 
    def memory_add(self):
        self.recall = self.recall + '+' + self.expression
 
    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)
 
    # Uses whatever is stored in memory_recall
 
    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)
 
    # Changes self.convert_constant to a string that allows degree conversion when button is clicked
 
    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad["foreground"] = 'white'
        self.btn_Deg["foreground"] = 'RED'
 
    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad["foreground"] = 'RED'
        self.btn_Deg["foreground"] = 'white'
 
    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")
 
    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up
 
splash_root = tk.Tk()
splash_root.title('Team 11 presents')
splash_root.geometry("650x490+450+150")



img = Image.open("calci.png")
resized_img = img.resize((650, 490))
my_img = ImageTk.PhotoImage(resized_img)
my_label = Label(image=my_img)
my_label.pack()
splash_root.after(3000, splash_root.destroy)
splash_root.mainloop()


root = tk.Tk()
Frame = Calculator(root) 
root.title("Scientific Calculator") 
root.geometry("650x490+450+150")
root.resizable(False, False)
root.mainloop()

