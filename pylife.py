from gui_utils.adaptor import GuiAdapter

from gui_utils.gui import Gui

if __name__ == "__main__":
    # creating Tk
    maingui = Gui()
    # passing Canvas to GuiAdapter
    adapter = GuiAdapter(maingui)
    # starting adaptor in another thread
    adapter.start()
    # looping Tk
    maingui.mainloop()
