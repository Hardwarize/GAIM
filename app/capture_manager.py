import mss
import pyautogui

class CaptureManager():
    def __init__(self):
        self.sct = mss.mss()
        self.game_window = self.__get_window()
        self.monitor = {"top": self.game_window.box.top, 
                        "left": self.game_window.box.left, 
                        "width": self.game_window.box.width, 
                        "height":self.game_window.box.height}
        
    def __get_window(self):
        windows_list = pyautogui.getAllWindows()
        game_window = next(filter(lambda x: x.title=='BlueStacks App Player', windows_list),None)
        return game_window

    def take_window_shot(self):
       image = self.sct.grab(self.monitor)
       return image