import turtle

turtle.bgcolor('green') #background color: green
gh = turtle.Turtle()  # gh = variable
gh.color('yellow', 'green')  # line color: yellow ; inside shape color = green
gh.shape('turtle')  # shape = turtle
# gh.pensize(40)  # pen size
gh.speed(10)  # drawing speed

gh.backward(100)
gh.left(90)
gh.backward(100)
gh.right(90)
gh.forward(100)

gh.right(90)
gh.forward(100)
gh.right(90)
gh.forward(100)

turtle.done()
