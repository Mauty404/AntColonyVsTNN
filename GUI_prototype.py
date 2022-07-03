from tkinter import LEFT, RIGHT
import matplotlib
import tkinter as tk
import TNNA as tnna
from matplotlib.figure import Figure
import Point_selector as ps
import ant_test as antcolony
matplotlib.use("TkAgg")


def Calculate():
    tnnaFinalDistance.set(round(tnna.CalculateSquence(int(parameter21.get())), 5))

    antColonyFinalDistance.set(round(antcolony.CalculateAntColony(parameter11.get(), parameter12.get()), 5))

    graph1Updated = tk.PhotoImage(file='AntColony.png')
    canvas1.itemconfig(canvas1Id, image=graph1Updated)

    graph2Updated = tk.PhotoImage(file='TNN.png')
    canvas2.itemconfig(canvas2Id, image=graph2Updated)

root = tk.Tk()

parameter11 = tk.StringVar(root, value="1")
parameter12 = tk.StringVar(root, value="1")
parameter21 = tk.StringVar(root, value="0")
antColonyFinalDistance = tk.StringVar(root, value="0")
tnnaFinalDistance = tk.StringVar(root, value="0")

root.geometry("1290x700")
root.minsize(1290, 700)
root.maxsize(1290, 700)
root.title("The salesman problem resolver")

frame11 = tk.Frame(root)
newPointsButton = tk.Button(frame11, text="Select new points", command=ps.OpenPointSelector, font=("Times New Roman", 15, "bold")).pack(side=LEFT, pady=5,
                                                                                                  padx=10, ipadx=10,
                                                                                                  ipady=5)
calculateButton = tk.Button(frame11, text="Calculate", command=Calculate, font=("Times New Roman", 15, "bold")).pack(side=RIGHT, ipadx=10, ipady=5)
frame11.grid(column=0, row=0)

title1Label = tk.Label(text="Ant colony optimization", font=("Times New Roman", 20, "bold")).grid(column=0, row=1)
f = Figure(figsize=(5, 5), dpi=100)
canvas1 = tk.Canvas(width=640, height=480)
graph1 = tk.PhotoImage(file='TNN_empty.png')
canvas1Id = canvas1.create_image(0, 0, image=graph1, anchor=tk.NW)
canvas1.grid(column=0, row=2, columnspan=2)
pathLength1Label = tk.Label(text="Length of path: ", font=("Times New Roman", 20, "bold")).grid(column=0, row=3)
pathLengthData1 = tk.Label(textvariable=antColonyFinalDistance, font=("Times New Roman", 20)).grid(column=1, row=3)

paramater11Label = tk.Label(text="Number of ants: ", font=("Times New Roman", 15, "bold")).grid(column=0, row=4)
parameter11Enter = tk.Entry(root, textvariable=parameter11, font=("Times New Roman", 13)).grid(column=1, row=4)

paramater12Label = tk.Label(text="Number of iterations: ", font=("Times New Roman", 15, "bold")).grid(column=0, row=5)
parameter12Enter = tk.Entry(root, textvariable=parameter12, font=("Times New Roman", 13)).grid(column=1, row=5)

title2Label = tk.Label(text="The nearest neighbour optimization", font=("Times New Roman", 20, "bold")).grid(column=4, row=1)
canvas2 = tk.Canvas(width=640, height=480)
graph2 = tk.PhotoImage(file='TNN_empty.png')
canvas2Id = canvas2.create_image(0, 0, image=graph2, anchor=tk.NW)
canvas2.grid(column=4, row=2, columnspan=4)

pathLength2Label = tk.Label(text="Length of path: ", font=("Times New Roman", 20, "bold")).grid(column=4, row=3)
pathLengthData2 = tk.Label(textvariable=tnnaFinalDistance, font=("Times New Roman", 20)).grid(column=5, row=3)

paramater21Label = tk.Label(text="Starting point number: ", font=("Times New Roman", 15, "bold")).grid(column=4, row=4)
parameter21Enter = tk.Entry(root, textvariable=parameter21, font=("Times New Roman", 13)).grid(column=5, row=4)

root.mainloop()
