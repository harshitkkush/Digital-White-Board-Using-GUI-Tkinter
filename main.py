#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Lybraries

import tkinter # main library - for GUI (Graphical User Interface)
from tkinter import * # main importing from tkinter - used in most functionalities
from tkinter import ttk # additional necessary importing - used in slider functionality
from tkinter import filedialog # additional necessary importing - used in save functionality
import PIL.ImageGrab as ImageGrab # additional necessary importing - used in save functionality
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

whiteboard  = Tk()
# The "root" of our projetc
# Instantiating the object Tk() of the class to the variable "whiteboard"
# So we can use all the functions of that object of the class through the variable "whiteboard"
# An object is a collection of variables and methods.

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Functions

# Value that is gonna be used on the slider - define initial value of it ass 1, to be  possible to draw
current_value = tkinter.DoubleVar(whiteboard, 1)

# Return the value readed on the slider
def get_current_value():
    return '{: .2}'.format(current_value.get())

# Define the color of what will be drawn
def set_color(new_color):
    global color, line_width, cursor_color

    color = new_color
    line_width = get_current_value() # It is the thickness of the pencil

# Locate the xy address of the point when you click with the mouse
def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y

# To "erase" when you draw (in other words, to draw with the background color)
def eraser():
    set_color('white')

# Draw when you press the mouse button and moved the mouse
def draw(work):
    global current_x, current_y

    line_width = get_current_value()

    # Basically it is going to draw a circle, but only the border of it on one point
    whiteboard_canvas.create_oval((current_x, current_y, work.x, work.y), outline= color, width=line_width)
    current_x = work.x
    current_y = work.y

# Creat the colours of the colour palette
def create_colour(position_y, c_opt):

    color = ''
    # Choose the colour based on the option

    if c_opt == 1 :
        color = 'black'
    elif c_opt == 2 :
        color = 'red'
    elif c_opt == 3:
        color = 'brown'
    elif c_opt == 4:
        color = 'blue'
    elif c_opt == 5:
        color = 'yellow'
    elif c_opt == 6:
        color = 'green'
    elif c_opt == 7:
        color = '#FFFFFE' # almost white

    # Create a rectangle with that colour on the right position    
    id = colour_palette_canvas.create_rectangle((12,position_y,42,position_y+30), fill=color)
    # Bind the click of the button 1 of the mouse with the set_color function with the current color
    colour_palette_canvas.tag_bind(id, '<Button-1>', lambda x: set_color(color))
    
# Clear all the canvas and rebuild it
def clear_all():
    c_opt = 1 # color option
    position_y = 10
    counter = 1

    whiteboard_canvas.delete('all')
    for counter in range(1, 8):
        create_colour(position_y, c_opt)
        c_opt += 1
        position_y += 40

# Save the image
def saveImage():
    # Choose a location to save the file
    fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")

    # Define the initial coordinates of the image to be saved
    x = whiteboard.winfo_rootx()+100
    y = whiteboard.winfo_rooty()+35

    # Define the final coordinates of the image to be saved
    img = ImageGrab.grab(bbox=(x,y,x+900,y+470))
    
    # Show the image saved
    img.show()

    # Save it
    img.save(fileLocation)

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
# Main

#-------------------------------------------------------------------------------------------------------------------
# Creating the whiteboard window



# Defining whiteboard parameters

# Title
whiteboard.title("Whiteboard")

# Dimensions and Position
whiteboard.geometry("1050x570+150+50")

# Locking the dimensions of the whiteboard
whiteboard.resizable(False, False) # Width and Height

# Background colour
whiteboard.configure(bg="#d3d3d3") # d3d3d3 -> hexadecimal to light gray color



# Creating the items of the whiteboard

# Whiteboard icon
whiteboard.iconbitmap(default="icon/whiteboard.ico")

# images
color_sidebar_image = PhotoImage(file="images/color_sidebar.png")
eraser_image = PhotoImage(file="images/eraser.png")
garbage_image = PhotoImage(file="images/garbage.png")
save_image = PhotoImage(file="images/save.png")

# slader
slider = ttk.Scale(whiteboard, from_=2, to=100, orient='horizontal', variable= current_value)
slider.place(x=100, y=525)

# labels
color_sidebar_label = Label(whiteboard, image=color_sidebar_image, bg="#d3d3d3")
color_sidebar_label.place(x=10, y=15)
slider_value_label = ttk.Label(whiteboard, text="thickness")
slider_value_label.place(x=210, y=530)

# Canvas
colour_palette_canvas = Canvas(whiteboard, bg="#ffffff", width=50, height=290, bd=0)
colour_palette_canvas.place(x=20, y=40)
whiteboard_canvas = Canvas(whiteboard, width=900, height=470, bg="#ffffff", cursor="dot blue")
whiteboard_canvas.place(x=100, y=35)

#buttons
eraser_button = Button(whiteboard, image=eraser_image, bg="#f2f3f5", command=eraser)
eraser_button.place(x=25, y=340)
garbage_button = Button(whiteboard, image=garbage_image, bg="#f2f3f5", command=clear_all)
garbage_button.place(x=25, y=395)
save_button = Button(whiteboard, image=save_image, bg="#f2f3f5", command=saveImage)
save_button.place(x=25, y=450)

# collours of the colour_palette_canvas
c_opt = 1 # color option
position_y = 10
counter = 1
for counter in range(1, 8):
    create_colour(position_y, c_opt)
    c_opt += 1
    position_y += 40
#-------------------------------------------------------------------------------------------------------------------

# Set the initial color of hte mouse
set_color('black')

# Bind the whiteboard canvas with the functions when the mouse is clicked os moved (with the button pressed)
whiteboard_canvas.bind('<Button-1>', locate_xy)
whiteboard_canvas.bind('<B1-Motion>', draw)

# Refresh the whiteboard and make it appear in looping
whiteboard.mainloop()

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------