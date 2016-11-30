import src.gui.grid_size_input as gsi
import src.gui.grid_window as gw

v=gsi.grid_size_input()
v.init([1,50])
v.start()
v.join()
g=gw.grid_window()
g.init([600,600],v.get_vars_as_int())
g.start()
g.join()
