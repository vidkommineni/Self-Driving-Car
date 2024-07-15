from turtle import*
import turtle
import time
import winsound
#from turtle import Screen, Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#clr = (0.60160,0,.9922)
#ending clr = (0.8633, .47660, .31255)


screen = turtle.Screen()
screen.setup(SCREEN_WIDTH + 220, SCREEN_HEIGHT + 20)
screen.title("Ending Screen!")
screen.bgcolor("light blue")
screen.bgpic('try123.gif')
screen.update()
def playmusic():
    winsound.PlaySound('birds_audio.wav', winsound.SND_ASYNC)

screen.listen() 
screen.onkeypress(playmusic, 'space')
#screen.onkeypress(None, 'Enter')
time.sleep(2)
screen.bgpic('bckgd.gif')
screen.tracer(False)
#turtle.textinput("HI")
turtle.done()
 