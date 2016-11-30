import src.utils as utils

class life_grid():
    def __init__(self,size,random=False):
        self.size=size
        self.grid=[]
        if random:
            self.generate_random()
        else:
            self.generate_empty()
        self.iter=0
    
    def evolve(self):
        new_grid=utils.cp_matrix(self.grid)
        for x in range(self.size[1]):
            for y in range(self.size[0]):
                if self.grid[x][y]==1:
                    count=0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if j!=0 or i!=0:
                                if x+i>=0 and y+j>=0 and x+i<len(self.grid) and y+j<len(self.grid[x]):
                                    if self.grid[x+i][y+j]==1:
                                        count+=1
                    if count!=2 and count!=3:
                        new_grid[x][y]=0
                else:
                    count=0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if j!=0 or i!=0:
                                if x+i>=0 and y+j>=0 and x+i<len(self.grid) and y+j<len(self.grid[x]):
                                    if self.grid[x+i][y+j]==1:
                                        count+=1
                    if count==3:
                        new_grid[x][y]=1
        self.grid=new_grid
        self.iter+=1
        
    def empty_copy(self):
        return [[None for i in range(self.size[0])] for j in range(self.size[1])]
    
    def generate_empty(self):
        self.grid=[[0 for i in range(self.size[0])] for j in range(self.size[1])]
        
    def generate_full(self):
        self.grid=[[1 for i in range(self.size[0])] for j in range(self.size[1])]
    
    def generate_random(self):
        self.grid=[[utils.bit_random() for i in range(self.size[0])] for j in range(self.size[1])]
        
    def fill(self,x,y):
        self.grid[x][y]=1
    
    def kill(self,x,y):
        self.grid[x][y]=0