from turtle import *
from random import *
from tkinter import *
from math import *

nombre_immeubles = 7
immeuble_x = 0
immeuble_y = 0
sol_y = int(window_height() / 4 * -1)
taille_etage = int((window_height() * 3 / 4 + 230) / 8)
sol_size = window_height() / 2 + sol_y

r = 0
g = 0
b = 0

root = Tk()

screen = Screen()
screen.setup(width=root.winfo_screenwidth(), height=root.winfo_screenheight())
screen.tracer(0)
root.destroy()

car = Turtle()
#car.hideturtle()
car.forward(50)
car.speed(0)


def couleur_aleatoire():
    colormode(255)
    global r
    global g
    global b
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)


def sol(y):
    penup()
    sety(y)


def immeuble(immeubles):
    im_distance_in_screen = window_width() / (immeubles * 3 + immeubles + 1)
    penup()
    setx(int(window_width() / 2 * -1))
    setheading(0)
    forward(im_distance_in_screen)
    for immeuble in range(0, immeubles):
        im_width = int(im_distance_in_screen * 3)
        im_etages = randint(3, 5)
        penup()
        couleur_aleatoire()
        color((int(r * (3 / 4)), int(g * (3 / 4)), int(b * (3 / 4))))
        starting_x = xcor()
        for etages in range(im_etages):
            pendown()
            begin_fill()
            color((int(r * (3 / 4)), int(g * (3 / 4)), int(b * (3 / 4))))
            fillcolor((r, g, b))
            setx(xcor() + im_width)
            sety(ycor() + taille_etage)
            setx(xcor() - im_width)
            sety(ycor() - taille_etage)
            if etages == 0:
                end_fill()
                porte(im_width)
            end_fill()
            if etages != 0:
                fenetres(3, im_width)
            setheading(90)
            forward(taille_etage)
        toit(im_width)
        setx(starting_x + im_width)
        setheading(0)
        forward(im_distance_in_screen)
        sety(sol_y - 30)


def fenetres(f_number, im_width):
    penup()
    im_starting_x = xcor()
    sety(ycor() + floor(taille_etage / 3))
    setx(int(xcor() + im_width / 16))
    window_size = int(im_width / 4)
    for f in range(f_number):
        color((0, 0, 0))
        pendown()
        begin_fill()
        setx(int(xcor() + window_size))
        sety(ycor() + taille_etage / 2.5)
        setx(int(xcor() - window_size))
        sety(ycor() - taille_etage / 2.5)
        setx(int(xcor() + window_size))
        fillcolor((153, 255, 255))
        end_fill()
        penup()
        f_type = randint(1, 3)
        if f_type == 2:
            setx(xcor() - 1)
            setx(ceil(xcor() - window_size / 2))
            pendown()
            sety(ycor() + taille_etage / 2.5)
            sety(ycor() - taille_etage / 5)
            setx(ceil(xcor() - window_size / 2))
            setx(ceil(xcor() + window_size - 1))
            penup()
            sety(ycor() - taille_etage / 5)
        if f_type == 3:
            pendown()
            setx(int(xcor() - window_size))
            setx(int(xcor() + window_size / 3))
            sety(ycor() + taille_etage / 2.5)
            setx(int(xcor() + window_size / 3))
            sety(ycor() - taille_etage / 2.5)
            setx(int(xcor() + window_size / 3) - 1)
            penup()
        setx(int(xcor() + im_width * 1 / 16))
    setx(im_starting_x)
    sety(ycor() - floor(taille_etage / 3))


def toit(im_width):
    color((0, 0, 0))
    fillcolor((0, 0, 0))
    pendown()
    setx(int(xcor() - im_width / 20))
    antennes = randint(0, 3)
    begin_fill()
    sety(ycor() + 15)
    setx(xcor() + im_width + int(2 * (im_width / 20)))
    sety(ycor() - 15)
    setx(xcor() - im_width + int(2 * (-im_width / 20)))
    end_fill()
    penup()
    sety(ycor() + 15)
    longueur_toit = im_width + int(2 * (im_width / 20))
    for loop in range(antennes):
        avance_random = randint(0, int(longueur_toit - 10))
        setx(xcor() + avance_random)
        pendown()
        longueur_antennes = randint(20, 50)
        sety(ycor() + longueur_antennes)
        sety(ycor() - longueur_antennes)
        setx(xcor() - avance_random)
    penup()


def porte(im_width):
    setheading(0)
    penup()
    sety(ycor() + 1)
    forward(int(im_width / 3))
    color((0, 0, 0))
    pendown()
    begin_fill()
    r_door = r
    g_door = g
    b_door = b
    if r * (5 / 4) <= 255:
        r_door = int(r * (5 / 4))
    else:
        r_door = int(r * (3 / 4))
    if g * (5 / 4) <= 255:
        g_door = int(g * (5 / 4))
    else:
        g_door = int(g * (3 / 4))
    if b * (5 / 4) <= 255:
        b_door = int(b * (5 / 4))
    else:
        b_door = int(b * (3 / 4))
    fillcolor((r_door, g_door, b_door))
    forward(int(im_width / 3))
    sety(ycor() + int(taille_etage / 1.4))
    setx(xcor() - int(im_width / 3))
    sety(ycor() - int(taille_etage / 1.4))
    end_fill()
    penup()
    sety(ycor() - 1)
    forward(int(im_width / 3 * -1))
    pendown()
    color((int(r * (3 / 4)), int(g * (3 / 4)), int(b * (3 / 4))))


def herbe():
    penup()
    colormode(255)
    color((0, 255, 0))
    setx(xcor() - int(window_width() / 2))
    pendown()
    pensize(2)
    begin_fill()
    sety(window_height() * -1)
    setx(window_width())
    sety(sol_y)
    setx(int(window_width() * -1))
    end_fill()
    begin_fill()
    fillcolor((33, 47, 60))
    color((33, 47, 60))
    setheading(-90)
    forward(sol_size / 4)
    setx(int(window_width()))
    setheading(-90)
    forward(sol_size / 2)
    setx(int(window_width() * -1))
    end_fill()
    color((255, 255, 255))
    setheading(90)
    forward(sol_size / 3.4)
    setheading(0)
    pensize(10)
    setx(int(window_width()))
    setx(int(window_width() * -1))
    pensize(3)
    penup()
    setx(int(window_width() / 2 * -1))
    sety(sol_y - 30)


def ciel():
    sol(sol_y)
    color("cyan")
    setx(int(window_width() / 2 * -1))
    sety(sol_y)
    pendown()
    setx(xcor() - int(window_width() / 2))
    pensize(2)
    begin_fill()
    sety(window_height())
    setx(window_width())
    sety(sol_y)
    setx(int(window_width()/2 * -1))
    end_fill()
    penup()
    color("black")
    setx(int((window_width()/2*(7/8)*-1)))
    sety(int(window_height()/2*(12/16)))
    pendown()
    color("yellow")
    begin_fill()
    dot(80)
    end_fill()
    dessineRayons(50, 40)
    right(45)
    dessineRayons(50, 40)
    left(45)


def dessineRayons(longueur, rayon):
    for i in range(4):
        penup()
        forward(rayon)
        pendown()
        forward(longueur)
        penup()
        backward(longueur + rayon)
        left(90)


def voiture(car, taille):
    car.pendown()
    car.fillcolor('orange')
    car.begin_fill()
    for i in range(2):
        car.forward(75*taille)
        car.left(90)
        car.forward(50*taille)
        car.left(90)
    car.end_fill()
    car.fillcolor('black')
    car.penup()
    car.begin_fill()
    car.setx(car.xcor() + 10*taille)
    for i in range(2):
        car.sety(car.ycor() - 20*taille)
        car.circle(10*taille)
        car.sety(car.ycor() + 20*taille)
        if i == 0:
            car.setx(car.xcor() + 55*taille)
    car.setx(car.xcor() - 65*taille)
    car.end_fill()
    car.forward(75*taille)
    car.pendown()
    car.fillcolor('orange')
    car.begin_fill()
    for i in range(2):
        car.forward(25*taille)
        car.left(90)
        car.forward(35*taille)
        car.left(90)
    car.end_fill()
    car.forward(-1*(75*taille))


def voiture_infini():
    car.sety(sol_y)
    car.forward(sol_size / 4)
    car.setheading(-90)
    car.forward(sol_size / 5)
    car.setheading(0)
    while True:
        car.clear()
        voiture(car, 1.7)
        screen.update()
        car.forward(0.5)
        if car.xcor() >= window_width()/2:
            car.setx((window_width() / 2)*-1)



def ville():
    global sol_y
    sol(sol_y)
    herbe()
    ciel()
    sety(sol_y-30)
    immeuble(int(nombre_immeubles))
    voiture_infini()


ville()
done()
