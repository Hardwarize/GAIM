import mss
from capture_manager import CaptureManager

if __name__ == "__main__":
    cm = CaptureManager()
    sct_img = cm.take_window_shot()
    print(sct_img)
