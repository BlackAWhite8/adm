import tkinter as tk
old = "10"
def updateinput(value):
    cc = {
        "x2":"bin",
        "x8":"oct",
        "x16":"hex"
        }
    current = str(entry.get())
    
    if current == "Error":
        current = ""
    
    if value == "C":
        entry.delete(0, tk.END)
        
    elif value == "x2" or value == "x8" or value == "x16":
        result = str(eval(current))
        val = cc[value]+'(' +result+ ')'
        result = str(eval(val)[2:])
        entry.delete(0, tk.END)
        entry.insert(0, result)
        global old
        old = value[1:]
        
    elif value == "x10":
        result = str(eval(current))
        result = int(result, int(old))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        
    elif value == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'x2', 'x8', 'x10', 'x16'
]


row = 1
col = 0

for button in buttons:
    tk.Button(root, text=button, width=10, height=3, command=lambda x=button: updateinput(x)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col >= 4:
        col = 0
        row += 1

root.mainloop()
