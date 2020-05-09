import tkinter as tk
import serial
from tkinter import messagebox


offsets = (
    (0, 0, 1, 0),  # top
    (1, 0, 1, 1),  # upper right
    (1, 1, 1, 2),  # lower right
    (0, 2, 1, 2),  # bottom
    (0, 1, 0, 2),  # lower left
    (0, 0, 0, 1),  # upper left
    (0, 1, 1, 1),  # middle
)
# Segments used for each digit; 0, 1 = off, on.
digits = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
)

class Digit:
    def __init__(self, canvas, x=10, y=10, length=20, width=4):
        self.canvas = canvas
        l = length
        self.segs = []
        for x0, y0, x1, y1 in offsets:
            self.segs.append(canvas.create_line(
                x + x0*l, y + y0*l, x + x1*l, y + y1*l,
                width=width, state = 'hidden'))
    def show(self, num):
        if num>=0:
            for iid, on in zip(self.segs, digits[num]):
                self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')
ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 38400
ser.open()
root = tk.Tk()
f = tk.Frame()
f1 = tk.Frame()
screen = tk.Canvas(root)
screen.pack(side='left')
screen.config(width=500, height=200)
tk.Label(f, text='Enter the number of votes allowed: ').pack(side = 'left')
tk.Label(f1, text='Please enter your ID: ').pack(side = 'left')
total = 0
total1 = 0
current_1 = "0"
current_2 = "0"
current_3 = "0"
ign = "0"
e = tk.Entry(f)
e.pack(side='left')
e.focus_set()
e1 = tk.Entry(f1)
e1.pack(side='left')
e1.focus_set()
f.pack(padx= 20, expand = True)
f1.pack(expand = True)
def toggle():
    ser.write(bytes([255]))

def callback():
    global total, total1
    total = e.get()
    total1 = int(total)
    if len(total) > 1:
        dig6.show(int(total[0]))
        dig7.show(int(total[1]))
    else:
        dig6.show(0)
        dig7.show(int(total))
        e.config(state='disabled')

b = tk.Button(f, text="Submit", width=10, command=callback)
b.pack(side='left')




## Voter 1
dig = Digit(screen, 40, 10) ##
lbl = tk.Label(screen,text = 'Candidate 1').place(x = 30,y = 60)
dig1 = Digit(screen, 70, 10) ##
dig.show(0)
dig1.show(0)

## Voter 2
dig2 = Digit(screen, 140, 10) ##
lbl1 = tk.Label(screen,text = 'Candidate 2').place(x = 130,y = 60)
dig3 = Digit(screen, 170, 10) ##
dig2.show(0)
dig3.show(0)

## Voter 3
dig4 = Digit(screen, 240, 10) ##
lbl2 = tk.Label(screen,text = 'Candidate 3').place(x = 230,y = 60)
dig5 = Digit(screen, 270, 10) ##
dig4.show(0)
dig5.show(0)

## Ignored
dig8 = Digit(screen, 340, 10) ##
lbl2 = tk.Label(screen,text = 'Ignored Votes').place(x = 330,y = 60)
dig9= Digit(screen, 370, 10) ##
dig8.show(0)
dig9.show(0)

## total votes remaining
dig6 = Digit(screen, 140,130) ##
lbl3 = tk.Label(screen,text = 'Votes Remaining').place(x = 120,y = 180)
dig7 = Digit(screen, 170,130) ##

def update_1():
    global current_1, current_2, current_3, total
    if (int(current_1)+int(current_2)+int(current_3)) < total1 and int(total) > 0:
         current_1 = str(int(current_1)+1)
         total = str(int(total)-1)
         if len(current_1) > 1:
             dig.show(int(current_1[0]))
             dig1.show(int(current_1[1]))
             if len(total) > 1:
                 dig6.show(int(total[0]))
                 dig7.show(int(total[1]))
             else:
                 dig6.show(0)
                 dig7.show(int(total))
         else:
             dig.show(0)
             dig1.show(int(current_1))
             if len(total) > 1:
                 dig6.show(int(total[0]))
                 dig7.show(int(total[1]))
             else:
                 dig6.show(0)
                 dig7.show(int(total))
    else:
        messagebox.showerror("Error", "Please enter a valid number of votes! or Max. No. of Votes Reached!")

def update_2():
    global current_1, current_2, current_3, total
    if (int(current_1)+int(current_2)+int(current_3)) < total1 and int(total) > 0:
         current_2 = str(int(current_2)+1)
         total = str(int(total)-1)
         if len(current_2) > 1:
             dig2.show(int(current_2[0]))
             dig3.show(int(current_2[1]))
             if len(total) > 1:
                 dig6.show(int(total[0]))
                 dig7.show(int(total[1]))
             else:
                 dig6.show(0)
                 dig7.show(int(total))
         else:
             dig2.show(0)
             dig3.show(int(current_2))
             if len(total) > 1:
                 dig6.show(int(total[0]))
                 dig7.show(int(total[1]))
             else:
                 dig6.show(0)
                 dig7.show(int(total))
    else:
        messagebox.showerror("Error", "Please enter a valid number of votes! or Max. No. of Votes Reached!")

def update_3():
    global current_1, current_2, current_3, total
    if (int(current_1)+int(current_2)+int(current_3)) < total1 and int(total) > 0:
         current_3 = str(int(current_3)+1)
         total = str(int(total)-1)
         if len(current_3) > 1:
             dig4.show(int(current_3[0]))
             dig5.show(int(current_3[1]))
             if len(total) > 1:
                 dig6.show(int(total[0]))
                 dig7.show(int(total[1]))
             else:
                 dig6.show(0)
                 dig7.show(int(total))
         else:
             dig4.show(0)
             dig5.show(int(current_3))
             if len(total) > 1:
                 dig6.show(int(total[0]))
                 dig7.show(int(total[1]))
             else:
                 dig6.show(0)
                 dig7.show(int(total))
    else:
        messagebox.showerror("Error", "Please enter a valid number of votes! or Max. No. of Votes Reached!")

def ignore():
        global current_1, current_2, current_3, ign, total
        if (int(current_1)+int(current_2)+int(current_3)+int(ign)) < total1 and int(total) > 0:
             ign = str(int(ign)+1)
             total = str(int(total)-1)
             if len(ign) > 1:
                 dig8.show(int(ign[0]))
                 dig9.show(int(ign[1]))
                 if len(total) > 1:
                     dig6.show(int(total[0]))
                     dig7.show(int(total[1]))
                 else:
                     dig6.show(0)
                     dig7.show(int(total))
             else:
                 dig8.show(0)
                 dig9.show(int(ign))
                 if len(total) > 1:
                     dig6.show(int(total[0]))
                     dig7.show(int(total[1]))
                 else:
                     dig6.show(0)
                     dig7.show(int(total))
        else:
            messagebox.showerror("Error", "Please enter a valid number of votes! or Max. No. of Votes Reached!")


b = tk.Button(screen, text="Vote", width=10, command=update_1).place(x=25, y=80)

b1 = tk.Button(screen, text="Vote", width=10, command=update_2).place(x=125, y=80)

b2 = tk.Button(screen, text="Vote", width=10, command=update_3).place(x=225, y=80)

b3 = tk.Button(screen, text="Ignore", width=10, command=ignore).place(x=325, y=80)

ids = ['01', '02', '03', '04']

def checkid():
    id_input = e1.get()
    if id_input in ids:
        ids.remove(id_input)
        toggle()
        messagebox.showinfo("Success", "You may cast your vote!")
    else:
        messagebox.showerror("Error", "ID not found in records. You may have conducted your vote before!")

b1 = tk.Button(f1, text="Submit", width=10, command=checkid)
b1.pack(side='left')


while(True):
    inp = ser.read()
    inp = int.from_bytes(inp, 'big')
    if (inp == 1):
          update_1()
          ser.write(bytes([0]))
    elif (inp == 2):
          update_2()
          ser.write(bytes([0]))
    elif (inp == 4):
          update_3()
          ser.write(bytes([0]))
           
                


