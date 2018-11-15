# -*- config: utf-8 -*-
# filename: main.py

import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title("KTW SPEED METER")
root.geometry("600x400")
print(font.families())

#Left Column Setting
left = tk.Frame(root, bg="white", relief="flat", bd=0)
left.pack(side="left", fill="both", expand=1)

lapLbl = tk.Label(left, text="5", bg="white", font=('','100',''))
lapLbl.pack(fill="both", expand=1)

sttBtn = tk.Button(left, text="開始", bg="lightgray", font=('','20',''))
rapBtn = tk.Button(left, text="周回", bg="lightgray", font=('','20',''))
finBtn = tk.Button(left, text="終了", bg="lightgray", font=('','20',''))
sttBtn.pack(fill="x", padx="20", pady="5", ipadx="5", ipady="10", expand=1)
rapBtn.pack(fill="x", padx="20", pady="5", ipadx="5", ipady="10", expand=1)
finBtn.pack(fill="x", padx="20", pady="5", ipadx="5", ipady="10", expand=1)

#Right Column Setting
right = tk.Frame(root, bg="blue", relief="flat", bd=0)
right.pack(side="right", fill="both", expand=1)

timeFrame = tk.Frame(right, bg="white", relief="flat", bd=0)
timeLeftFrame  = tk.Frame(timeFrame, bg="white", relief="flat", bd=0)
timeRightFrame = tk.Frame(timeFrame, bg="white", relief="flat", bd=0)
timeFrame.pack(fill="both", expand=1)
timeLeftFrame.pack(side="left", fill="both", expand=1)
timeRightFrame.pack(side="right", fill="both", expand=1)

speedFrame = tk.Frame(right, bg="white", relief="flat", bd=0)
speedFrame.pack(side="bottom", fill="both", expand=1)

allTimeMenuLbl = tk.Label(timeLeftFrame, text="全", bg="white", relief="groove" , bd=4, font=('','30',''))
rapTimeMenuLbl = tk.Label(timeLeftFrame, text="周", bg="white", relief="groove" , bd=4, font=('','30',''))
dlyTimeMenuLbl = tk.Label(timeLeftFrame, text="遅", bg="white", relief="groove" , bd=4, font=('','30',''))

allTimeLbl = tk.Label(timeRightFrame, text="00:00:00", bg="white", font=('','60',''))
rapTimeLbl = tk.Label(timeRightFrame, text="00:00:00", bg="white", font=('','60',''))
dlyTimeLbl = tk.Label(timeRightFrame, text="00:00:00", bg="white", font=('','60',''))

allTimeMenuLbl.pack(fill="both", expand=1, ipadx=15, ipady=15, padx=15, pady=15)
rapTimeMenuLbl.pack(fill="both", expand=1, ipadx=15, ipady=15, padx=15, pady=15)
dlyTimeMenuLbl.pack(fill="both", expand=1, ipadx=15, ipady=15, padx=15, pady=15)
allTimeLbl.pack(fill="both", expand=1)
rapTimeLbl.pack(fill="both", expand=1)
dlyTimeLbl.pack(fill="both", expand=1)

speedLbl = tk.Label(speedFrame, text="25.0km/h", bg="white", font=('','80',''))
speedLbl.pack(side="bottom", fill="both", expand=1)

root.mainloop()