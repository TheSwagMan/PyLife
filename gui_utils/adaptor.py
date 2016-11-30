from threading import Thread


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
