from threading import Thread
import tkinter
import gui.grid_canvas as gc
import objects.life_grid as lg
import game.main_game as mg

class grid_window(Thread):
    def init(self,win_size,grid_size):
        self.win_size=win_size
        self.grid_size=grid_size
        self.right_area_size=[80,self.win_size[1]]
        self.bottom_arrea_size=[self.win_size[0],80]
        self.canvas_size=[self.win_size[0]-self.right_area_size[0],self.win_size[1]-self.bottom_arrea_size[1]]
        
    def run(self):
        self.main_game=mg.main_game()
        self.game_win=tkinter.Tk()
        self.game_win.title("Pylife")
        self.game_win.minsize(self.win_size[0], self.win_size[1])
        self.game_win.maxsize(self.win_size[0], self.win_size[1])
        
        self.main_frame=tkinter.Frame(self.game_win,width=self.grid_size[0]+self.right_area_size[0],height=self.right_area_size[1])
        
        self.main_canvas=gc.grid_canvas(self.main_frame,self.canvas_size,lg.life_grid(self.grid_size))
        self.right_frame=tkinter.Frame(self.main_frame,width=self.right_area_size[0],height=self.right_area_size[1])
        
        self.bottom_frame=tkinter.Frame(self.game_win,width=self.bottom_arrea_size[0],height=self.bottom_arrea_size[1])
        
        self.pause_button=tkinter.Button(self.right_frame,text="Play",command=self.toogle_play)
        self.random_button=tkinter.Button(self.right_frame,text="Random",command=self.random_grid)
        self.clear_button=tkinter.Button(self.right_frame,text="Clear",command=self.clear_grid)
        self.fill_button=tkinter.Button(self.right_frame,text="Fill",command=self.fill_grid)
        self.main_label=tkinter.Label(self.right_frame,text="Hi main !")
        
        self.time_label=tkinter.Label(self.bottom_frame,text="Hi time !")
        self.time_button_up=tkinter.Button(self.bottom_frame,text="+",command=self.more_time)
        self.time_button_down=tkinter.Button(self.bottom_frame,text="-",command=self.less_time)
        
        self.main_frame.pack(side=tkinter.TOP,fill=tkinter.BOTH)
        self.main_canvas.pack(side=tkinter.LEFT)
        self.right_frame.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)
        self.bottom_frame.pack(side=tkinter.BOTTOM,fill=tkinter.BOTH)
        
        self.pause_button.pack(fill=tkinter.BOTH)
        self.random_button.pack(fill=tkinter.BOTH)
        self.clear_button.pack(fill=tkinter.BOTH)
        self.fill_button.pack(fill=tkinter.BOTH)
        self.main_label.pack(fill=tkinter.BOTH)
        
        self.time_label.pack(side=tkinter.LEFT)
        self.time_button_up.pack(side=tkinter.LEFT)
        self.time_button_down.pack(side=tkinter.LEFT)
        
        self.main_game.init(self.main_canvas,self.main_label,self.time_label)
        self.main_game.start()
        
        self.game_win.protocol("WM_DELETE_WINDOW", self.close)
        self.game_win.bind('<Escape>', self.close_callback)
        
        self.game_win.mainloop()
        
    def toogle_play(self):
        if self.main_game.is_playing:
            self.pause_button.config(text="Play")
        else:
            self.pause_button.config(text="Pause")
        self.main_game.toogle_play()
    
    def random_grid(self):
        self.main_canvas.random_grid()
        self.refresh_grid()
        
    def clear_grid(self):
        self.main_canvas.clear_grid()
        self.refresh_grid()
    
    def fill_grid(self):
        self.main_canvas.fill_grid()
        self.refresh_grid()
        
    def refresh_grid(self):
        self.main_canvas.refresh()
        
    def close_callback(self,event):
        self.close()
    
    def more_time(self):
        self.main_game.add_time_inter(0.1)
    
    def less_time(self):
        self.main_game.add_time_inter(-0.1)
    
    def close(self):
        self.game_win.destroy()