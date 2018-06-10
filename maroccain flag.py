import turtle

m = turtle.Turtle() #give m the value of turtle
turtle.title("morocain flag by marwankous!")#title of the window
turtle.setup(950, 500)#window size
turtle.bgcolor("red") #define background color
m.shape("arrow")   #define the chape of pen
m.speed("slowest")#define speed of turtle
m.ht()# hide turtle
m.pensize(30);m.pencolor("green") #define pen size and color
m.pu();m.lt(90);m.fd(40);m.lt(90);m.fd(150);m.rt(180) 
m.pd() #define start position
for _ in range(5): #drawing the star
   m.fd(300);m.rt(144)
m.pu()#put down the pen
m.goto(250,-160)#go to signature position
m.pencolor("black")#set the signature color to black
m.write("by marwankous", align="left",font=("fantasy", 15, "bold"))#my signature
turtle.done() #to let the wondow open after finish drawing