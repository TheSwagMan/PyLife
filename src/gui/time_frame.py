import tkinter

class time_frame():
    def __init__(self,parent,size):
        self.parent=parent
        self.size=size
        self.main_frame=tkinter.Frame(self.parent,parent,width=size[0],height=size[0])
        self.main_frame.pack(fill=tkinter.X,expand=True)
        closeButton=tkinter.Button(self.main_frame, text="Close")
        closeButton.pack(side=tkinter.RIGHT, padx=5, pady=5)
        okButton = tkinter.Button(self.main_frame, text="OK")
        okButton.pack(side=tkinter.RIGHT)