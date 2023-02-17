from turtle import *
speed("fastest")
pencolor("blue")
fillcolor("yellow")
pensize(2)
side= 8
for i in range(side):
    fd(100)
    begin_fill()
    for i in range(side):
        fd(25)
        for i in range(side):
            fd(75/2)
            lt(360/side)
            dot(20) 
        rt(360/side)
hideturtle()
mainloop()    
    
    
        