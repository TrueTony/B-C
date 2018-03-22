# сложность
# время хода компьютера 1 сек.
# сорц https://python-scripts.com/tkinter-introduction
from PIL import *
from tkinter import *
from tkinter.ttk import Style

 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent
        self.parent.title('Быки и Коровы')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def centerWindow(self):
        w = 650
        h = 550

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def initUI(self):
        #self.style = Style()
        #self.style.theme_use('default')
        #self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text='Quit', command = self.quit)
        quitButton.place(x=50, y=50)
    
        
def main():
    root = Tk()
    app = Example(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()