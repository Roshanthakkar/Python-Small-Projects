from turtle import*
from random import randrange
from freegames import square,vector

food=vector(0,0)
sanke=[vector(10,0)]
aim=vector(0,-10)

# this is 2 dimensional game and pass two parmeters pass karya che
def change (x,y):
    aim.x=x
    aim.y=y

def inside(haead):
    return-200 <head. x<190 and -200 <head.y <190
    
# move the sanke 
def move():
    head=sanke[-1].copy()
    head.move(aim)

    if not inside(head)or head in sanke:
        square(head.x,head.y,9,'red')
        update()
        return

    sanke.append()

    if head==food:
        print('snake',len(sanke))
        food.x=randrange(-15,15)*10
        food.y=randrange(-15,15)*10

    else:
        sanke.pop()

    clear()

    for body in sanke:
        square(body.x,body.y,9,'green')

    square(food.x,food.y,9,'red')
    update()
    ontimer(move,100)

    hideturtle()
    tracer(False)
    listen()
    onkey(lambda:change(10,0),'right')
    onkey(lambda:change(-10,0),'left')
    onkey(lambda:change(0,10),'Up')
    onkey(lambda:change(0,-10),'Down')

    move()
    done()
    
