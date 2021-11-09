import turtle

turtle.bgcolor('green')
gh = turtle.Turtle()  # gh = variable
gh.color('yellow', 'green')  # line color: yellow ; background color = green
gh.shape('turtle')  # shape = turtle
# gh.pensize(40)  # pen size
gh.speed(10)  # drawing speed

for x in range(5): #repeat 5 times
    gh.left(72) #turn left 72 degree
    gh.forward(100)

    gh.right(144) #turn right 144 degree
    gh.forward(100)

turtle.mainloop()
