from threading import Thread
import tkinter

class grid_size_input(Thread):
    def __init__(self, valid_range=[]):
        super().__init__()
        self.wwidth=300
        self.wheight=300
        self.is_closed=False
        self.force_valid=valid_range!=[]
        self.valid_range=valid_range
        self.size=None

    def run(self):
        self.win=tkinter.Tk()
        self.win.title("Size ?")
        self.win.maxsize(self.wwidth,self.wheight)
        self.spin_x=tkinter.Spinbox(self.win, from_=0, to=50)
        self.spin_y=tkinter.Spinbox(self.win, from_=0, to=50)
        self.ok_button=tkinter.Button(self.win,text="Ok",command=self.close)
        self.spin_x.pack()
        self.spin_y.pack()
        self.ok_button.pack()
        self.win.protocol("WM_DELETE_WINDOW", self.close)
        self.win.bind('<Escape>', self.close_callback)
        self.win.bind('<Return>', self.close_callback)
        self.win.mainloop()
    
    def close_callback(self,event):
        self.close()
    
    def close(self):
        self.size=(self.spin_x.get(),self.spin_y.get())
        if self.force_valid:
            if not self.input_is_valid():
                return
        self.is_closed=True
        self.win.destroy()
    
    def input_is_valid(self):
        if self.size[0].isdigit() and self.size[1].isdigit():
            if int(self.size[0])>=self.valid_range[0] and int(self.size[0])<=self.valid_range[1] and int(self.size[1])>=self.valid_range[0] and int(self.size[1])<=self.valid_range[1]:
                return True
        return False
    
    def get_vars(self):
        if self.size!=None:
            return self.size
        return None
    
    def get_vars_as_int(self):
        if self.size!=None:
            if self.size[0].isdigit() and self.size[1].isdigit():
                return [int(i) for i in self.size]
        return None