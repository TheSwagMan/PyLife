import tkinter,shutil,subprocess,os
import objects.life_grid as lg

CANVAS_SAVE_DIR="saved_canvas"
class grid_canvas():
    def __init__(self,parent,size,grid=lg.life_grid((1,1)),color_dead="white",color_alive="black"):
        self.alive_cell_tag="a_cell"
        self.last_hit=[]
        self.grid=grid
        self.rect_grid=grid.empty_copy()
        self.parent=parent
        self.size=size
        self.color_dead=color_dead
        self.color_alive=color_alive
        self.main_canvas=tkinter.Canvas(self.parent,width=self.size[0],height=self.size[1],bg=self.color_dead)
        self.main_canvas.bind('<Button-1>', self.toogle_cell_click)
        self.main_canvas.bind('<B1-Motion>', self.toogle_cell_motion)
        self.refresh()
        
    def toogle_cell_motion(self,event):
        try:
            if event.x>=0 and event.x<self.size[0] and event.y>=0 and event.y<self.size[1]:
                self.toogle_cell(event,False)
        except:
            print(event.x,event.y)
            
    def toogle_cell_click(self,event):
        self.toogle_cell(event,True)

    def toogle_cell(self,event,key):
        col_width=self.size[0]/self.grid.size[0]
        row_height=self.size[1]/self.grid.size[1]
        col=int(event.y/col_width)
        row=int(event.x/row_height)
        if [col,row]!=self.last_hit or key:
            if not self.rect_grid[row][col]:
                self.grid.fill(row,col)
            else:
                self.grid.kill(row,col)
        self.refresh()
        self.last_hit=[col,row]
        
    def set_grid(self,grid):
        self.grid=grid
    
    def refresh(self):
        cx,cy=0,0
        self.main_canvas.delete("all")
        self.main_canvas.delete(self.main_canvas.find_withtag(self.alive_cell_tag))
        for y in range(self.grid.size[0]):
            for x in range(self.grid.size[1]):
                if self.grid.grid[x][y]:
                    self.rect_grid[x][y]=self.main_canvas.create_rectangle(cx,cy,cx+self.size[0]/self.grid.size[1],cy+self.size[1]/self.grid.size[0],fill=self.color_alive,outline=self.color_dead,tags=self.alive_cell_tag)
                else:
                    self.rect_grid[x][y]=None
                cx=cx+self.size[0]/self.grid.size[1]
            cx=0
            cy=cy+self.size[1]/self.grid.size[0]
            
    def save_canvas(self,file_name):
        if not os.path.isdir(CANVAS_SAVE_DIR):
            os.mkdir(CANVAS_SAVE_DIR)
        self.main_canvas.postscript(file=CANVAS_SAVE_DIR+"/"+file_name, colormode='color')
    
    def evolve(self):
        self.grid.evolve()
    
    def get_iter(self):
        return self.grid.iter
    
    def clear_grid(self):
        self.grid.generate_empty()
    
    def fill_grid(self):
        self.grid.generate_full()
    
    def random_grid(self):
        self.grid.generate_random()
        
    def pack(self,**kwargs):
        self.main_canvas.pack(kwargs)