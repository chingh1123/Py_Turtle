import turtle

turtle.bgcolor('green')
gh = turtle.Turtle()  #gh = variable
gh.color('yellow', 'green') #line color: yellow ; background color: green
gh.shape('turtle') #shape = turtle
gh.pensize(40) #pen size
gh.speed(10)  #drawing speed

gh.forward(200)  #line no.1 walk straight
gh.left(90)  #line no.1 turn left 90 degree

gh.forward(200)  #line no.2 walk straight
gh.left(90)  #line no.2 turn left 90 degree

gh.forward(200)  #line no.3 walk straight
gh.left(90)  #line no.3 turn left 90 degree

gh.forward(200)  #line no.4 walk straight
gh.left(90)  #line no.4 turn left 90 degree

turtle.done() #finish the running
