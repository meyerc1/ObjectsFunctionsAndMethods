"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Carson Meyer.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    window = rg.RoseWindow(500, 500)

    center_point_a = rg.Point(150 , 150)
    center_point_b = rg.Point(300, 300)
    circle_a_radius = 64
    circle_b_radius = 169
    circle_a = rg.Circle(center_point_a, circle_a_radius)
    circle_b = rg.Circle(center_point_b, circle_b_radius)
    circle_a.fill_color = 'red'
    circle_a.attach_to(window)
    circle_b.attach_to(window)
    window.render()

    window.close_on_mouse_click()


    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    window = rg.RoseWindow(500, 500)

    circle1_point = rg.Point(250,250)
    rectangle1_corner1 = rg.Point(350, 350)
    rectangle1_corner2 = rg.Point(50, 50)

    circle1_radius = 121



    circle1 = rg.Circle(circle1_point, circle1_radius)
    rectangle1 = rg.Rectangle(rectangle1_corner1, rectangle1_corner2)

    circle1.attach_to(window)
    rectangle1.attach_to(window)

    circle1.fill_color= 'midnight blue'

    window.render()

    print('circle1 fill color',circle1.fill_color)
    print('circle1 center', circle1_point)
    print('x coordinate =', 250)
    print('y coordinate =', 250)

    rectangle1_center = 200

    print('Rectangle not filled!')
    print('Center of Rectangle', rectangle1_center, rectangle1_center)
    print('x coordinate =', rectangle1_center)
    print('y coordinate =', rectangle1_center)

    window.close_on_mouse_click()



    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    window = rg.RoseWindow(500, 500)

    line1 = rg.Line(rg.Point(150, 150), rg.Point(50, 30))
    line2 = rg.Line(rg.Point(350, 350), rg.Point(10, 10))

    line1.thickness = 30

    line1.attach_to(window)
    line2.attach_to(window)

    line1.pen = rg.Pen('black', 30)

    window.render()

    print('midpoint', line2.get_midpoint())
    print('x coordinate of midpoint', line2.get_midpoint())
    print('y coordinate of midpoint', line2.get_midpoint())

    window.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
