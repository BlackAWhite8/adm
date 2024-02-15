import tkinter as tk

def main():
    
    def toBASEint(num, base):
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = abs(num)
        b = alpha[n % base]
        while n >= base:
            n = n // base
            b += alpha[n % base]
        return ('' if num >= 0 else '-') + b[::-1]


    def toBaseFrac(frac, base, n=16):
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b = ''
        while n:
            frac *= base
            frac = round(frac, n)
            b += str(alpha[int(frac)])
            frac -= int(frac)
            n -= 1
        return b


    def convert():
        try:
            Number = number_entry.get()
            Basein = int(basein_entry.get())
            Baseout = int(baseout_entry.get())
        except:
            result_label.config(text="missed parametrs")
            return
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if '.' in Number:
            num, frac = map(str, Number.split('.'))
            num = int(num, Basein)
            a = toBASEint(num, Baseout)
            b = 0
            k = Basein
            for i in frac:
                b += alpha.index(i) / k
                k *= Basein
            b = str(toBaseFrac(b, Baseout)).rstrip('0')
            result_label.config(text=a + '.' + b)
        else:
            result_label.config(text=toBASEint(int(Number, Basein), Baseout))


# Create the main window
    root = tk.Tk()
    root.title("Base Converter")

    # Create input fields
    number_label = tk.Label(root, text="Number:")
    number_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    number_entry = tk.Entry(root)
    number_entry.grid(row=0, column=1, padx=5, pady=5)

    basein_label = tk.Label(root, text="Base in:")
    basein_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    basein_entry = tk.Entry(root)
    basein_entry.grid(row=1, column=1, padx=5, pady=5)

    baseout_label = tk.Label(root, text="Base out:")
    baseout_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    baseout_entry = tk.Entry(root)
    baseout_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create convert button
    convert_button = tk.Button(root, text="Convert", command=convert)
    convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Create result label
    result_label = tk.Label(root, text="")
    result_label.grid(row=4, column= 0, columnspan=2, padx=5, pady=5)

    # Start the main loop
    root.mainloop()

if __name__ == '__main__':
    main()
