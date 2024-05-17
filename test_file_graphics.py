from graphics import *


win = GraphWin("Inches to Meters Converter", 500, 150)
win.setBackground(color="lightgray")

# Input prompt
input_prompt = Text(Point(55, 20), "Inches: ")
input_prompt.draw(win)
input_prompt.setSize(15)


# Input field
input_field = Entry(Point(225, 20), 25)
input_field.draw(win)


# Convert Button (create text then the border)
convert_btn = Text(Point(415, 20), "Convert")
convert_btn.draw(win)
convert_btn.setSize(15)

convert_btn_border = Rectangle (Point(380, 10), Point(450, 30))
convert_btn_border.setWidth(2)
convert_btn_border.draw(win)


# Result Label
result_label = Text(Point(55, 100), "Meters: ")
result_label.draw(win)
result_label.setSize(15)


# Loop to make the button functional
try:
    mouse = win.getMouse()
except GraphicsError:
    quit()  # if the user closes the window quit

while True:
     # coordinates for convert_btn_border
    if 380 < mouse.getX() < 450 and 10 < mouse.getY() < 30:

        # Get input value and convert
        if input_field.getText():  # only convert to float if string is not empty
            inches = float(input_field.getText())
        else:
            try:
                mouse = win.getMouse()
            except GraphicsError:
                break
            
            continue

        meters = round(inches / 39.37, 4)

        # Clear result display
        try:
            result_value.undraw()  # if result_value exists it will be undrawn
        except:
            pass

        # Display Result
        result_value = Text(Point(200, 100), meters)
        result_value.draw(win)
        result_value.setSize(15)

    # Get the coordinates of the mouse
    try:
        mouse = win.getMouse()
    except GraphicsError:  # an error is created when the user closes the window then "getMouse()" is called
        break              # if this happens break out of the loop


# Why are you using graphics.py?
# Just use tkinter by its self, it's so much better.