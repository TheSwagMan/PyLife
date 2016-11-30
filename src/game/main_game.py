from threading import Thread
import time

class main_game(Thread):
    def __init__(self, canvas, main_label, time_label):
        super().__init__()
        self.main_canvas=canvas
        self.main_label=main_label
        self.time_label=time_label
        self.iter=0
        self.time_interval=0.2
        self.is_playing=False
        self.is_closed=False
    
    def run(self):
        self.refresh_iter_disp()
        while not self.is_closed:
            self.refresh_time_disp()
            if self.is_playing:
                self.refresh_iter_disp()
                self.main_canvas.evolve()
                self.main_canvas.refresh()
            time.sleep(self.time_interval)
    
    def toogle_play(self):
        self.is_playing=not self.is_playing
    
    def set_time_interval(self,t):
        self.time_interval=t
        self.display_time(str(self.time_interval)+" s")
    
    def display_time(self,s):
        self.time_label.configure(text=s)
    
    def display_main(self,s):
        self.main_label.configure(text=s)
    
    def refresh_iter_disp(self):
        self.display_main(str(self.main_canvas.get_iter()))
    
    def refresh_time_disp(self):
        self.display_time(str(self.time_interval)+" s")
    
    def add_time_inter(self,v):
        if self.time_interval+v>0.0 and self.time_interval+v<=5.0:
            self.time_interval=round(self.time_interval+v,1)
            self.refresh_time_disp()
        
    def close(self):
        self.is_closed=True