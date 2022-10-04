import mss
import pyautogui
if __name__ == "__main__":
    a = pyautogui.getAllWindows()
    b = next(filter(lambda x: x.title=='BlueStacks App Player', a),None)
    b
    with mss.mss() as sct:
        monitor = {"top": b.box.top, "left": b.box.left, "width":b.box.width, "height":b.box.height}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
