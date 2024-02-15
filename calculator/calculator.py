import tkinter as tk
import converter as cr

def toBASEint(num, base=10):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base]
    while n >= base:
        n = n // base
        b += alpha[n % base]
    return ('' if num >= 0 else '-') + b[::-1]


def toBaseFrac(frac, base=10, n=16):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n:
        frac *= base
        frac = round(frac, n)
        b += str(alpha[int(frac)])
        frac -= int(frac)
        n -= 1
    return b

def convert(Number,Basein):
    try:
        Baseout = 10
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if '.' in Number:
            num, frac = map(str, Number.split('.'))
            num = int(num, Basein)
            b = 0
            k = Basein
            for i in frac:
                b += alpha.index(i) / k
                k *= Basein
            b = str(toBaseFrac(b, Baseout)).rstrip('0')
            result = str(num) + '.' + b
            return float(result)
        else:
            result =int(Number, Basein)
            return float(result)
    except:
        raise ValueError




        
def add():
    try:
        num1 = number1_entry.get()
        num2 = number2_entry.get()
        basein1 = int(basein_entry1.get())
        basein2 = int(basein_entry2.get())
    except ValueError:
        if basein_entry1.get() == '' or basein_entry2.get() == '':
            basein1 = 10
            basein2 = 10
        else:
            answer_label.config(text="Error")
            return 
    try:
        answer_label.config(text=(convert(num1,basein1) + convert(num2,basein2)))
    except:
        answer_label.config(text="Error")
             
def subtraction():
    try:
        num1 = number1_entry.get()
        num2 = number2_entry.get()
        basein1 = int(basein_entry1.get())
        basein2 = int(basein_entry2.get())
    except ValueError:
        if basein_entry1.get() == '' or basein_entry2.get() == '':
            basein1 = 10
            basein2 = 10
        else:
            answer_label.config(text="Error")
            return 
    try:
        answer_label.config(text=(convert(num1,basein1) - convert(num2,basein2)))
    except:
        answer_label.config(text="Error")
def division():
    try:
        num1 = number1_entry.get()
        num2 = number2_entry.get()
        basein1 = int(basein_entry1.get())
        basein2 = int(basein_entry2.get())
    except ValueError:
        if basein_entry1.get() == '' or basein_entry2.get() == '':
            basein1 = 10
            basein2 = 10
        else:
            answer_label.config(text="Error")
            return 
    try:
        answer_label.config(text=(convert(num1,basein1) / convert(num2,basein2)))
    except ZeroDivisionError:
        print("делить на ноль нельзя")
        answer_label.config(text="Error")
    except:
        answer_label.config(text="Error")
            
#Mul        
def multiplay():
    try:
        num1 = number1_entry.get()
        num2 = number2_entry.get()
        basein1 = int(basein_entry1.get())
        basein2 = int(basein_entry2.get())
    except ValueError:
        if basein_entry1.get() == '' or basein_entry2.get() == '':
            basein1 = 10
            basein2 = 10
        else:
            answer_label.config(text="Error")
            return 
    try:
        answer_label.config(text=(convert(num1,basein1) * convert(num2,basein2)))
    except:
        answer_label.config(text="Error")
        

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create 1
number1_label = tk.Label(root, text="Number 1:")
number1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
number1_entry = tk.Entry(root)
number1_entry.grid(row=0, column=1, padx=5, pady=5)

basein_label1 = tk.Label(root, text="Base in:")
basein_label1.grid(row=1, column=0, padx=5, pady=5, sticky="e")
basein_entry1 = tk.Entry(root)
basein_entry1.grid(row=1, column=1, padx=5, pady=5)



# Create 2
number2_label = tk.Label(root, text="Number 2:")
number2_label.grid(row=0, column=3, padx=5, pady=5, sticky="e")
number2_entry = tk.Entry(root)
number2_entry.grid(row=0, column=4, padx=5, pady=5)

basein_label2 = tk.Label(root, text="Base in:")
basein_label2.grid(row=1, column=3, padx=5, pady=5, sticky="e")
basein_entry2 = tk.Entry(root)
basein_entry2.grid(row=1, column=4, padx=5, pady=5)

equel_label = tk.Label(root, text="=")
equel_label.grid(row=0, column=5, padx=5, pady=5, sticky="e")

sum_button = tk.Button(root, text="+", command = add)
sum_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")

sub_button = tk.Button(root, text="-", command = subtraction)
sub_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")

div_button = tk.Button(root, text="/", command = division)
div_button.grid(row=2, column=2, padx=5, pady=5, sticky="e")

mul_button = tk.Button(root, text="*", command = multiplay)
mul_button.grid(row=3, column=2, padx=5, pady=5, sticky="e")

answer_label = tk.Label(root, text="Answer :")
answer_label.grid(row=0, column=6, padx=5, pady=5, sticky="e")

converter_btn = tk.Button(root, text="open converter", command = cr.main)
converter_btn.grid(row=2, column=5, padx=5, pady=5, sticky="e")

# Start the main loop
root.mainloop()
