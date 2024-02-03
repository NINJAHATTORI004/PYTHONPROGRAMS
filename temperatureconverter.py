#6
import tkinter as tk
def convert():
        temp=float(entry.get())
        converted_temp=0.0
        if var.get()==1:
            converted_temp=(temp*9/5)+32
        elif var.get()==2:
            converted_temp=(temp-32)*5/9
        elif var.get()==3:
            converted_temp=temp+273.15
        elif var.get()==4:
            converted_temp=temp-273.15
        elif var.get()==5:
            converted_temp=(temp+459.67)*5/9
        elif var.get()==6:
            converted_temp=(temp*9/5)-459.67
        
        label.config(text="converted Temperature:"+str(converted_temp))
root=tk.Tk()
root.title("Temperature converter")
entry=tk.Entry(root)
entry.pack()
var=tk.IntVar()
celsius_to_fahrenheit=tk.Radiobutton(root,text="celsius to Fahrenheit",variable=var,value=1)
celsius_to_fahrenheit.pack()
fahrenheit_to_celsius=tk.Radiobutton(root,text="Fahrenheit to celsius",variable=var,value=2)
fahrenheit_to_celsius.pack()
celsius_to_kelvin=tk.Radiobutton(root,text="celsius to kelvin",variable=var,value=3)
celsius_to_kelvin.pack()
kelvin_to_celsius=tk.Radiobutton(root,text="kelvin to celsius",variable=var,value=4)
kelvin_to_celsius.pack()
fahrenheit_to_kelvin=tk.Radiobutton(root,text="fahrenheit to kelvin",variable=var,value=5)
fahrenheit_to_kelvin.pack()
kelvin_to_fahrenheit=tk.Radiobutton(root,text="kelvin to fahrenheit",variable=var,value=6)
kelvin_to_fahrenheit.pack()
button=tk.Button(root,text="convert",command=convert)
button.pack()
label=tk.Label(root,text="conveted Temperature")
label.pack()
root.mainloop()
