#Ivana Maria
#4/3/26
#P4LAB1_MariaIvana
#use turtle and loops to draw

#import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# set turtle options
pen.pensize(5)
win.bgcolor("pink")
pen.pencolor("purple")
pen.shape("arrow")

#code to draw the shape 
for side in range(4):
    pen.forward(100)
    pen.left(90)

#move triangle to top of the square 
pen.left(90)
pen.forward(100)
pen.right(90)

#while loop that execute 3 times 
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1 

#keeps window open 
win.mainloop()