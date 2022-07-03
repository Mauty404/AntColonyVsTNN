import matplotlib.pyplot as plt
from matplotlib.widgets import LassoSelector

plt.rcParams['toolbar'] = 'None'

xData = []
yData = []

def onSelect(x):
    print()

def on_click(event):
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        xData.append(round(event.xdata))
        yData.append(round(event.ydata))
        f = open("coor.txt", "w")
        for item in xData:
            f.write("%s/" % item)
        f.write("\n")
        for item in yData:
            f.write("%s/" % item)
        f.close()
        plt.clf()
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.plot(xData, yData, 's')
        plt.draw()


def OpenPointSelector():

    xData.clear()
    yData.clear()

    fig, ax = plt.subplots()

    plt.xlim(0,100)
    plt.ylim(0,100)

    lineprops = {'color': 'red', 'linewidth': 4, 'alpha': 0.8}
    lasso = LassoSelector(ax = ax, onselect=onSelect, lineprops=lineprops, button=1)
    plt.connect('button_press_event', on_click)

    fig.show()