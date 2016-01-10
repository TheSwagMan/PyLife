import sys

sys.path.append('src/')

import gui.grid_size_input as gsi
import gui.grid_canvas as gc
import objects.life_grid as lg
import game.main_game as mg
import gui.grid_window as gw
import tkinter
import time

v=gsi.grid_size_input()
v.init([1,50])
v.start()
v.join()
g=gw.grid_window()
g.init([600,600],v.get_vars_as_int())
g.start()
g.join()