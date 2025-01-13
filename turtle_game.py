import turtle
import colorsys
import random

# הגדרת המסך
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("ספירלה צבעונית עם Turtle")

# יצירת הצב
spiral = turtle.Turtle()
spiral.speed(0)  # מהירות מקסימלית
spiral.width(2)

# מספר הצבעים בספירלה
num_colors = 360
hue = 0

# פונקציה לצביעת הספירלה
def draw_spiral():
    global hue
    for i in range(360):
        # חישוב צבע באמצעות מערכת הצבעים HSV
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        spiral.pencolor(color)
        spiral.forward(i * 0.5)
        spiral.left(59)  # זווית סיבוב ליצירת הספירלה
        hue += 1/num_colors
        if hue > 1:
            hue = 0

# קריאת הפונקציה לציור הספירלה
draw_spiral()

# סיום התצוגה
spiral.hideturtle()
turtle.done()
