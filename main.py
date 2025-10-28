from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

master = Tk()
master.geometry("750x750")
master.title("Rysowanie z plików")

def fileOpen():
    filePath = filedialog.askopenfilename()
    fileChosen = open(filePath,"r")
    fileData = fileChosen.read()
    
    linesIn = fileData.splitlines()

    xValues = []
    yValues = []

    for line in linesIn:
        partsOf = line.split()
        xValues.append(float(partsOf[0]))
        yValues.append(float(partsOf[1]))

    yLargest = max(yValues)
    xLargest = xValues[yValues.index(yLargest)]
    
    yValLeft = yValues[:yValues.index(yLargest)]
    yValRight = yValues[yValues.index(yLargest):]

    yhalfLargest = yLargest / 2

    firstLeftY = min(yValLeft, key=lambda x: abs(x - yhalfLargest))
    firstLeftX = xValues[yValues.index(firstLeftY)]
    if firstLeftY > yhalfLargest:
        secondLeftY = yValues[yValues.index(firstLeftY) - 1]
        secondLeftX = xValues[yValues.index(secondLeftY)]
    elif firstLeftY < yhalfLargest:
        secondLeftY = yValues[yValues.index(firstLeftY) + 1]
        secondLeftX = xValues[yValues.index(secondLeftY)]


    firstRightY = min(yValRight, key=lambda x: abs(x - yhalfLargest))
    firstRightX = xValues[yValues.index(firstRightY)]
    if firstRightY > yhalfLargest:
        secondRightY = yValues[yValues.index(firstRightY) + 1]
        secondRightX = xValues[yValues.index(secondRightY)]
    elif firstRightY < yhalfLargest:
        secondRightY = yValues[yValues.index(firstRightY) - 1]
        secondRightX = xValues[yValues.index(secondRightY)]
      
    leftA = (secondLeftY - firstLeftY) / (secondLeftX - firstLeftX)
    leftB = secondLeftY - leftA * secondLeftX
    
    rightA = (secondRightY - firstRightY) / (secondRightX - firstRightX)
    rightB = firstRightY - rightA * firstRightX

    leftX = (yhalfLargest - leftB) / leftA
    rightX = (yhalfLargest - rightB) / rightA

    figureObj, axisObj = plt.subplots(figsize=(5, 5))

    xMinimum = min(xValues)
    xMaximum = max(xValues)
    axisObj.set_xlim(xMinimum,xMaximum)
    
    axisObj.plot([leftX,rightX],[yhalfLargest,yhalfLargest],color="purple",linestyle="dashed",linewidth=2)
    axisObj.text(leftX+0.025,yhalfLargest,f"współczynnik = {round((rightX-leftX)*100,3)}")
    
    axisObj.plot(xValues,yValues)
    axisObj.scatter(xLargest,yLargest, color="green")
    axisObj.text(xLargest,yLargest,f"{xLargest}, {yLargest}")

    figureDraw = FigureCanvasTkAgg(figureObj, master=master)
    figureDraw.get_tk_widget().place(x=100, y=0) 
    figureDraw.draw()

buttonOpen = ttk.Button(master, text="Otwórz plik", width=10, command=lambda: fileOpen())
buttonOpen.place(x=0,y=0)

master.mainloop()