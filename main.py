#Simple calculator
import customtkinter as ctk

def display(value):
    global equation_text
    equation_text += str(value)
    equation_label.set(equation_text) #Adding elements to the equation

def calc():
    global equation_text
    try:
        result = eval(equation_text)
        equation_label.set(str(result))
        equation_text = str(result)  # Store result for further calculations
    except Exception as e:
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = ctk.CTk()
window.title("Calculator")
window.geometry('300x440')

equation_text = ""
equation_label = ctk.StringVar()

#Display label
label = ctk.CTkLabel(master=window, width=300, height=70, font=('Arial', 20), text_color='black', textvariable=equation_label, corner_radius=1, bg_color='lightgrey')
label.pack()

#Frame for buttons
frame = ctk.CTkFrame(master=window, width=300, height=420)
frame.pack()

#Buttons
button1 = ctk.CTkButton(master=frame, text="1", width=70, height=70, command=lambda: display(1))
button1.grid(column=0, row=0, padx=2, pady=2)

button2 = ctk.CTkButton(master=frame, text="2", width=70, height=70, command=lambda: display(2))
button2.grid(column=1, row=0, padx=2, pady=2)

button3 = ctk.CTkButton(master=frame, text="3", width=70, height=70, command=lambda: display(3))
button3.grid(column=2, row=0, padx=2, pady=2)

button4 = ctk.CTkButton(master=frame, text="4", width=70, height=70, command=lambda: display(4))
button4.grid(column=0, row=1, padx=2, pady=2)

button5 = ctk.CTkButton(master=frame, text="5", width=70, height=70, command=lambda: display(5))
button5.grid(column=1, row=1, padx=2, pady=2)

button6 = ctk.CTkButton(master=frame, text="6", width=70, height=70, command=lambda: display(6))
button6.grid(column=2, row=1, padx=2, pady=2)

button7 = ctk.CTkButton(master=frame, text="7", width=70, height=70, command=lambda: display(7))
button7.grid(column=0, row=2, padx=2, pady=2)

button8 = ctk.CTkButton(master=frame, text="8", width=70, height=70, command=lambda: display(8))
button8.grid(column=1, row=2, padx=2, pady=2)

button9 = ctk.CTkButton(master=frame, text="9", width=70, height=70, command=lambda: display(9))
button9.grid(column=2, row=2, padx=2, pady=2)

button0 = ctk.CTkButton(master=frame, text="0", width=144, height=70, command=lambda: display(0))
button0.grid(column=1, row=3, padx=2, pady=2, columnspan=2)

clear_button = ctk.CTkButton(master=frame, text="AC", width=70, height=70, command=clear)
clear_button.grid(column=0, row=3, padx=2, pady=2)

plus = ctk.CTkButton(master=frame, text="+", width=70, height=70, command=lambda: display('+'))
plus.grid(column=3, row=0, padx=2, pady=2)

minus = ctk.CTkButton(master=frame, text="-", width=70, height=70, command=lambda: display('-'))
minus.grid(column=3, row=1, padx=2, pady=2)

multiply = ctk.CTkButton(master=frame, text="x", width=70, height=70, command=lambda: display('*'))
multiply.grid(column=3, row=2, padx=2, pady=2)

divide = ctk.CTkButton(master=frame, text="÷", width=70, height=70, command=lambda: display('/'))
divide.grid(column=3, row=3, padx=2, pady=2)

equal = ctk.CTkButton(master=frame, text="=", width=144, height=70, command=calc)
equal.grid(column=2, row=4, padx=2, pady=2, columnspan=2)

window.mainloop()
