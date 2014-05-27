import Tkinter
import time
from Canny import Canny
import sobel
try:
    import Image
except ImportError:
    print 'PIL not found. You cannot view the image'
import os

#creating a global scope variable for the file name and execution time
s = 'filename'
global_time = 0.00


class simpleapp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        #put the label PATH here
        self.labelVariable = Tkinter.StringVar()
        self.labelVariable.set("File:")
        label = Tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="w", fg= "white", bg="blue")
        label.grid(column=0, row=0, columnspan=1, sticky='EW')
        


        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=1, row=0, sticky='EW', columnspan=3)
        self.entry.bind("<Return>", self.OnPressEnter)
        

        button = Tkinter.Button(self, text= "Sobel", command=self.OnButtonClick)
        button.grid(column=1, row=1)

        button = Tkinter.Button(self, text= "Canny", command = self.OnCannyClick)
        button.grid(column=2, row=1)

        #global label
        label = Tkinter.Label(self, anchor="w", fg= "white", bg="blue")
        label.grid(column=0, row=3, columnspan=3, sticky='EW')
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        #pass
    def OnButtonClick(self):
        print "You Clicked Sobel"
        global s
        s = self.entry.get()
        #print s
        if s == '':
            print "Enter filename"
        else:
            time_start = time.time()
            sobel.sobelFunction(s+'.jpg')
            timer = time.time() - time_start
            print "time of execution for Sobel: " + str(timer)
            #self.label.set("time of execution for Sobel: " + str(timer))
    def OnPressEnter(self, event):
        print "Please select an algorithm"
    def OnCannyClick(self):
        print "You selected Canny"
        global s
        s = self.entry.get()
        #print s
        if s == '':
            print "Enter filename"
        else:
            time_start = time.time()
            canny = Canny(s+'.jpg', 1.4, 50, 100)
            timer = time.time() - time_start
            print "Time of execution for Canny: " + str(timer)
            #self.label.set("time of execution for Canny: " + str(timer))
            im = canny.grad
        #Image.fromarray(im).show()

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Project GUI')
    app.mainloop()
    
