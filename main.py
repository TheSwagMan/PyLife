from utils.adaptor import GuiAdapter

from utils.gui import Gui

if __name__ == "__main__":
    # creating Tk
    maingui = Gui()
    # passing Canvas to GuiAdapter
    adapter = GuiAdapter(maingui)
    # starting adaptor in another thread
    adapter.start()
    # looping Tk
    maingui.mainloop()
