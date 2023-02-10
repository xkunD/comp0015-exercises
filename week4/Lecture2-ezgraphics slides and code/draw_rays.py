from ezgraphics import GraphicsWindow

WIDTH = 500
HEIGHT = 300

    
def draw_rays_block(canvas, x, y, width, height, num_lines):

    canvas.drawRectangle(x, y, width, height)

    increment = height / num_lines
    
    for i in range(1, num_lines + 1):
        canvas.drawLine(x, y, x + width, y + (i * increment))



    
def main():

    # Create a graphics window (WIDTH x HEIGHT pixels):
    win = GraphicsWindow(WIDTH, HEIGHT)

    # Access the canvas contained in the graphics window:
    canvas = win.canvas()

    draw_rays_block(canvas, 0, 0, WIDTH / 2, HEIGHT / 2, 5)
    draw_rays_block(canvas, WIDTH / 2, HEIGHT / 2, (WIDTH / 2) - 1, (HEIGHT / 2) - 1, 5)


    # Wait for the user to close the window
    win.wait()

    
    

if __name__ == "__main__":
    main()
