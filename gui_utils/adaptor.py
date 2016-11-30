from threading import Thread
import src.gui.grid_size_input as gsi
import src.gui.grid_window as gw
import src.game.main_game as mg

class GuiAdapter(Thread):
    def __init__(self, window):
        super().__init__()
        self._window = window

    def get_window(self):
        return self._window

    def run(self):
        """
        Put your starting code here.
        """
        v = gsi.grid_size_input()
        v.init([1, 50])
        v.start()
        v.join()
        self._grid_win = gw.grid_window(self.get_window(), [600, 600], v.get_vars_as_int())
        self._main_game = mg.main_game(self._grid_win.get_canvas(), *self._grid_win.get_labels())
        self._main_game.start()
        self._grid_win.set_callers(
            [self._main_game.add_time_inter, self._main_game.is_playing, self._main_game.toogle_play,
             self._main_game.close])
        self._main_game.join()
        while not self._grid_win.is_closed:
            pass

    def onclose(self, *args):
        pass
