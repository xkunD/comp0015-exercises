from ezgraphics import GraphicsWindow




def main():

    # Create a graphics window (640 x 480 pixels):
    win = GraphicsWindow(640, 480)

    # Access the canvas contained in the graphics window:
    canvas = win.canvas()
    canvas.drawRect(15, 10, 20, 30)

    # Wait for the user to close the window
    win.wait()

    
    

if __name__ == "__main__":
    main()
