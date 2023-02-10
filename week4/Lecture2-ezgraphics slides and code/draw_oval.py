from ezgraphics import GraphicsWindow

WIDTH = 500
HEIGHT = 300
MARGIN = 40
    
def draw_oval_block(canvas, x, y, width, height):
    
    canvas.drawRectangle(x, y, width, height)

    canvas.setFill("yellow")
    
    canvas.drawOval(x + MARGIN / 2, y + MARGIN / 2, width - MARGIN, height - MARGIN)

    canvas.setFill("")

    canvas.drawLine(x, y, x + width, y + height)

    canvas.drawLine(x + width, y, x, y + height) 


    
def main():

    # Create a graphics window (WIDTH x HEIGHT pixels):
    win = GraphicsWindow(WIDTH, HEIGHT)

    # Access the canvas contained in the graphics window:
    canvas = win.canvas()

    draw_oval_block(canvas, 0, 0, WIDTH / 2, HEIGHT / 2)

    # 
    draw_oval_block(canvas, WIDTH / 2, HEIGHT / 2, (WIDTH / 2) - 1,\
                    (HEIGHT / 2) - 1)


    # Wait for the user to close the window
    win.wait()

    
    

if __name__ == "__main__":
    main()
