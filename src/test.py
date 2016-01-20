__author__ = 'R4M80'
from threading import Thread
import tkinter
import time

class winjeuvie(Thread):                                        #   Classe pour la fenetre du jeu implementant le multithreading
    def init(self):                                             #   fonction d'initialisation
        self.wwidth=600                                         #   definitions des variables de base de la classe
        self.wheight=600
        self.grow_factor=100
        self.is_closed=False
        self.alive_cell_color="black"
        self.dead_cell_color="white"
        self.grid=[]
        self.size=[]
        self.iter=0
        self.is_set=False
        self.is_playing=False
        self.time_interval=0.2

    def run(self):                                              #   fonction a lancer dans un thread externe
        g_choose=grid_chooser()
        while not g_choose.get_grid():
            g_choose.init()
            g_choose.run()
        self.grid=g_choose.get_grid()
        self.size=[len(self.grid),len(self.grid[0])]
        self.win=tkinter.Tk()                                   #   creation d'une fenetre Tk
        self.win.title("Jeu de la Vie")                         #   changement du titre de la fenetre
        self.win.minsize(self.wwidth,self.wheight)              #   taille de la fenetre
        self.win.maxsize(self.wwidth+self.grow_factor,self.wheight+self.grow_factor)
        self.lbl_1=tkinter.Label(self.win,text="",wraplength=500) # creation d'un affichage de texte
        self.canvas_1=tkinter.Canvas(self.win,width=self.wwidth,height=self.wheight,bg=self.dead_cell_color) # creation d'un canevas pour l'affichage des cellules
        self.pause_button=tkinter.Button(self.win,text="Play",command=self.toogle_play)
        self.time_frame=tkinter.Frame(self.win)
        self.time_input=tkinter.Spinbox(self.time_frame,increment=0.1,from_=0,to=2,)
        self.time_lbl=tkinter.Label(self.time_frame,text=str(self.time_interval)+" s")
        self.time_ok_button=tkinter.Button(self.time_frame,text="Ok",command=self.refresh_time)
        self.time_input.pack(side=tkinter.LEFT)
        self.time_lbl.pack(side=tkinter.RIGHT)
        self.time_ok_button.pack(side=tkinter.BOTTOM)
        self.lbl_1.pack()                                       #   on affiche le texte
        self.canvas_1.pack()                                    #   affichage du canvas
        self.pause_button.pack()
        self.time_frame.pack()
        self.win.protocol("WM_DELETE_WINDOW", self.close)       #   recuperation de l'evenement de fermeture de la fenetre
        self.win.bind('<Escape>',self.close)                    #   extinction lors du clic de la touche <echap>
        self.draw_grill()
        self.is_set=True
        self.win.mainloop()                                     #   boucle princiaple

    def draw_grill(self):                                       #   fonction d'affichage d'une grille
        if not self.is_closed:                                  #   si la fenetre est toujours ouverte
            cx,cy=0,0                                           #   variable de position de la cellule tracee
            self.canvas_1.delete("all")                         #   nettoyage du canvas
            for y in range(len(self.grid)):                        #   parcours de la grille a afficher
                for x in range(len(self.grid[y])):
                    if self.grid[y][x]:                            #   si la cellule est vivante, on l'affiche
                        self.canvas_1.create_rectangle(cx,cy,cx+self.wwidth/len(self.grid[y]),cy+self.wheight/len(self.grid),fill=self.alive_cell_color,outline=self.dead_cell_color)
                    cx=cx+self.wwidth/len(self.grid[y])            #   on deplace le curseur de rectangle
                cx=0                                            #   on a fini la ligne, donc on initialise un des curseurs
                cy=cy+self.wheight/len(self.grid)                  #   on incremente l'autre
        self.display_text(self.iter)

    def refresh_time(self):
        try:
            self.time_interval=float(self.time_input.get())
            self.time_lbl.configure(text=str(self.time_interval)+" s")
        except:
            print("Bad entry")

    def display_text(self,t):                                   #   fonction d'affichage d'un texte
        if not self.is_closed:                                  #   si la fenetre est toujours ouverte
            self.lbl_1.configure(text=t)                        #   on change le texte de l'afficheur

    def save_canvas(self,file_name):
        self.canvas_1.postscript(file=file_name, colormode='color')

    def next_day(self):                                            #    fonction de viellissement de grille
        self.iter+=1
        nouvelle_grille=cp_grille(self.grid)                       #   on fait une copie de la grille
        for x in range(self.size[0]):                            #   parcours des lignes
            for y in range(self.size[1]):                     #   parcours des cases
                if self.grid[x][y]==1:                            ##   si la case contient une cellule vivante
                    count=0                                     #   compteur de cases vivantes presentes autour
                    for i in range(-1,2):                       #   on parcours les cases autour
                        for j in range(-1,2):
                            if j!=0 or i!=0:                    #   on evite la case du milieu
                                if x+i>=0 and y+j>=0 and x+i<len(self.grid) and y+j<len(self.grid[x]):
                                    if self.grid[x+i][y+j]==1:     #   si la case est pleine
                                        count+=1                #   on incremente
                    if count!=2 and count!=3:                   #   si la cellule n'a pas assez ou trop de cellules vivantes autour
                        nouvelle_grille[x][y]=0                 #   elle meurt
                else:                                          ##   si la case ne contient pas de cellule vivante
                    count=0                                     #   compteur de cases vivantes presentes autour
                    for i in range(-1,2):                       #   on parcours les cases autour
                        for j in range(-1,2):
                            if j!=0 or i!=0:                    #   on evite la case du milieu
                                if x+i>=0 and y+j>=0 and x+i<len(self.grid) and y+j<len(self.grid[x]):
                                    if self.grid[x+i][y+j]==1:     #   si la case est pleine
                                        count+=1                #   on incremente
                    if count==3:                                #   si la cellule a assez de cellules vivantes autour
                        nouvelle_grille[x][y]=1                 #   elle nait
        self.grid=nouvelle_grille

    def toogle_play(self):
        self.is_playing=not self.is_playing

    def close(self):                                            #   fonction de fermeture de la fenetre
        self.is_closed=True                                     #   on change la variable is_closed en True
        self.canvas_1.destroy()
        self.lbl_1.destroy()
        self.win.destroy()                                      #   on detruit la fenetre

class grid_chooser(Thread):
    grid=[]
    def init(self):
        self.wwidth=600                                         #   definitions des variables de base de la classe
        self.wheight=600
        self.grow_factor=100
        self.is_closed=False
        self.alive_cell_color="black"
        self.dead_cell_color="white"
        self.grid=[]
        self.rect_grid=[]
        self.grid_size=[]
        self.last_hit=[]

    def run(self):
        c=grid_size_chooser()
        while not c.get_vars():
            c.init()
            c.run()
        self.grid_size=c.get_vars()
        self.grid=[[0 for i in range(self.grid_size[0])] for j in range(self.grid_size[1])]
        self.rect_grid=[[None for i in range(self.grid_size[0])] for j in range(self.grid_size[1])]
        self.win=tkinter.Tk()                                   #   creation d'une fenetre Tk
        self.win.title("Choix de la grille - Jeu de la Vie")    #   changement du titre de la fenetre
        self.win.minsize(self.wwidth,self.wheight)              #   taille de la fenetre
        self.win.maxsize(self.wwidth+self.grow_factor,self.wheight+self.grow_factor)
        self.canvas_1=tkinter.Canvas(self.win,width=self.wwidth,height=self.wheight,bg=self.dead_cell_color) # creation d'un canevas pour l'affichage des cellules
        self.ok_button=tkinter.Button(self.win,text="Ok",command=self.validate)
        self.canvas_1.pack()                                    #   affichage du canvas
        self.ok_button.pack()
        cx,cy=0,0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.canvas_1.create_rectangle(cx,cy,cx+self.wwidth/len(self.grid[i]),cy+self.wheight/len(self.grid),fill=self.dead_cell_color,outline=self.alive_cell_color)
                cx=cx+self.wwidth/len(self.grid[i])
            cx=0
            cy=cy+self.wheight/len(self.grid)
        self.canvas_1.bind("<B1-Motion>", self.toogle_cell_motion)
        self.canvas_1.bind("<Button-1>", self.toogle_cell_click)
        self.win.protocol("WM_DELETE_WINDOW", self.close)       #   recuperation de l'evenement de fermeture de la fenetre
        self.win.bind('<Escape>', self.close)                   #   extinction lors du clic de la touche <echap>
        self.win.mainloop()                                     #   boucle princiaple

    def toogle_cell_motion(self,event):
        self.toogle_cell(event,False)

    def toogle_cell_click(self,event):
        self.toogle_cell(event,True)

    def toogle_cell(self,event,key):
        col_width=self.canvas_1.winfo_width()/self.grid_size[0]
        row_height=self.canvas_1.winfo_height()/self.grid_size[1]
        col=int(event.x/col_width)
        row=int(event.y/row_height)
        if [col,row]!=self.last_hit or key:
            if not self.rect_grid[row][col]:
                self.grid[row][col]=1
                self.rect_grid[row][col]=self.canvas_1.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
            else:
                self.grid[row][col]=0
                self.canvas_1.delete(self.rect_grid[row][col])
                self.rect_grid[row][col]=None
        self.last_hit=[col,row]

    def validate(self):
        self.close()

    def close(self):                                            #   fonction de fermeture de la fenetre
        self.is_closed=True                                     #   on change la variable is_closed en True
        self.canvas_1.destroy()
        self.win.destroy()                                      #   on detruit la fenetre

    def get_grid(self):
        if self.grid==[]:
            return None
        else:
            return self.grid

class grid_size_chooser(Thread):
    size=[]
    def init(self):
        self.wwidth=200
        self.wheight=200
        self.is_closed=False
        self.size=[]

    def run(self):
        self.win=tkinter.Tk()                                   #   creation d'une fenetre Tk
        self.win.title("Choix de la taille de la grille - Jeu de la Vie")    #   changement du titre de la fenetre
        self.win.maxsize(self.wwidth,self.wheight)              #   taille de la fenetre
        self.spin_x=tkinter.Spinbox(self.win, from_=0, to=50)   #   input de x
        self.spin_y=tkinter.Spinbox(self.win, from_=0, to=50)   #   input de y
        self.ok_button=tkinter.Button(self.win,text="Ok",command=self.validate)
        self.spin_x.pack()
        self.spin_y.pack()
        self.ok_button.pack()
        self.win.protocol("WM_DELETE_WINDOW", self.close)       #   recuperation de l'evenement de fermeture de la fenetre
        self.win.bind('<Escape>', self.close)                   #   extinction lors du clic de la touche <echap>
        self.win.mainloop()

    def validate(self):
        self.size=[int(self.spin_x.get()),int(self.spin_y.get())]
        self.close()

    def get_vars(self):
        if self.size==[]:
            return None
        else:
            return self.size

    def close(self):
        self.is_closed=True                                     #   on change la variable is_closed en True
        self.win.destroy()                                      #   on detruit la fenetre

def cp_grille(grille):
    """
    :param: grille a copier
    :return: nouvelle copie de la grille entree
    fonction de copie de grille
    """
    r=[]                                                        #   on initialise la variable
    for i in range(len(grille)):                                #   on parcours la grille
        r.append([])                                            #   on rajoute une ligne
        for j in range(len(grille[i])):
            r[i].append(grille[i][j])                           #   on remplit les colones avec les valeurs de l'argument entre
    return grille                                                    #   on retourne la copie

g=winjeuvie()
g.init()
g.start()
while True:
    if g.is_set:
        if g.is_playing:
            g.next_day()
            g.draw_grill()
        time.sleep(g.time_interval)
        if g.is_closed:
            exit(0)
