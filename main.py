# MAIN.PY
from graphics import Window  # import the window class


# our main loop function
def main():
    win = Window(800, 600)  # create a window
    win.wait_for_close()  # close it on call of this method


# Need this to run!
if __name__ == "__main__":
    main()
