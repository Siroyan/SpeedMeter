# -*- config: utf-8 -*-
# filename: main.py

import tkinter as tk

root = tk.Tk()
root.title("KTW SPEED METER")
root.geometry("600x400")

left = tk.Frame(root, bg="yellow", relief="flat", bd=0)
left.pack(side="left", fill="both", expand=1)

speedLabel = tk.Label(left, text="25", bg="green", font=('','50',''))
speedLabel.pack(fill="x", expand=1)

right = tk.Frame(root, bg="blue", relief="flat", bd=0)
right.pack(side="right", fill="both", expand=1)

timeLabel = tk.Label(right, text="00:00:00", bg="green", font=('','50',''))
timeLabel.pack(fill="x", expand=1)


root.mainloop()