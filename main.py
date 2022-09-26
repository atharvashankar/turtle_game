from turtle import *

rt(-90)

def up():
	fd(100)

def d():
	rt(45)

def a():
	lt(45)

def right():
	rt(90)

def left():
	lt(90)

listen()

onkey(up,'Up')
onkey(down,'Down')
onkey(right,'Right')
onkey(left,'Left')
onkey(d,'d')
onkey(a,'a')


done()