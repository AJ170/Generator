import ttkbootstrap as tb
import random


#Put each safety tip into list
lines = open('SafetyTips.txt').read().splitlines()


root = tb.Window(
    title='Random Saftey Tip Generator', 
    size=(600, 200), # Size of window
    themename='darkly', 
    position=(930, 400)) # Starting pos of window

random_text = tb.Label(
    master=root,
    text='', 
    font=('Helvetica', 18), 
    wraplength=500)

random_text.pack(pady=30)


def randomize():
    random_text.config(text=random.choice(lines))


button_style = tb.Style()
button_style.configure(
    'warning.TButton', 
    font=('Helvetica', 19))

btn=tb.Button(master=root, text="Generate Saftey Tip", command=randomize, style="warning.TButton")
btn.pack()


root.mainloop()