# - BUGS -
# - LIST INDEX OUT OF RANGE
# - PUTTING BRACKETS ON THE ITEM

from Tkinter import *
from Tkinter import Checkbutton
import os
import platform
import csv

        
class App(object):
    
    def __init__(self, master):
        self.master = master
        self.master 
        self.frame = Frame(master)
        self.frame.grid()
        self.addFrame = Frame(master)
        self.addFrame.grid(row=0, column=0, columnspan=2, sticky='N')
        self.listFrame = Frame(master)
        self.listFrame.grid(row=1, column=0, columnspan=2, sticky='NW')
        self.todoList = []
        self.buttonList = []
        self.initUI()
        self.loadFile()
    
    
    def loadFile(self):
        print "<- LOADING FILE ->"
        with open(self.fileName, 'rb') as tdl:
            reader = csv.reader(tdl, delimiter=' ', quotechar='|')
            for n in reader:
                print n
                self.addCheckButton(n)
        tdl.close
    
    def initUI(self):
        
        if platform.system() == 'Darwin':
            self.fileName='/Users/matthewgarsteck/ownCloud/Code/todoList/todoList.csv'
        else:
            self.fileName='/home/matthew/ownCloud/Code/todoList/todoList.csv'
            
        self.entryBox = Entry(self.frame, width = 15)
        self.entryBox.grid(row=0, column=0, sticky='N')
        
        self.addButton = Button(self.frame, text="<-ADD->", command=lambda: self.addCheckButton(self.entryBox.get()))
        self.addButton.grid(row=0, column=1, sticky='N')
        
        if len(self.todoList) == 0:
            self.label1 = Label(self.listFrame, text="<- NOTHING SCHEDULED ->")
            self.label1.grid(row=0, column=0, sticky="N")
        
        
        
    def saveData(self, todoList):
        with open(self.fileName, 'wb') as tdl:
            writer = csv.writer(tdl, delimiter=' ', quotechar='|')
            for n in todoList:
                writer.writerow([n])
        tdl.close
                   
    def removeCheckButton(self, buttonNum):
        self.buttonList[buttonNum].destroy()
        # - NOT WORKING
        del self.todoList[buttonNum]
        del self.buttonList[buttonNum]
        self.saveData(self.todoList)
        if len(self.todoList) == 0:
            self.label1.grid(row=0, column=1, sticky='N')
            
    def addCheckButton(self, item):
        self.entryBox.delete(0, END)
        self.label1.grid_forget()
        self.todoList.append(item)
        
        n = len(self.buttonList)
        lx = Checkbutton(self.listFrame, text=self.todoList[n], variable=self.todoList[n], command=lambda ni=n: self.removeCheckButton(ni))
        lx.grid(row=n, column=0, sticky='NW')
        self.buttonList.append(lx)
        #print self.buttonList
        self.saveData(self.todoList)
        
root = Tk()
root.wm_title('ToDo List')
#root.geometry("250x300")
app = App(root)
root.mainloop()
