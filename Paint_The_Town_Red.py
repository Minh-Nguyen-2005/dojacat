#File's name: Paint_The_Town_Red
#Author: Minh Nguyen
#Date: 09/15/2023
#Purpose: Intro to cs1lib
#Course: CS1 - Intro to Programming and Computation-01-02
#Description: Art created by me displays my idol Doja Cat performing her hit Paint The Town Red on the VMAs

from cs1lib import *

def mydraw(): # This main draw function must not take any parameters
    #background: paint the town red!
    set_clear_color(1, 0, 0)
    clear()

    set_stroke_color(0, 0, 0) #black
    #draw hair
    set_fill_color(0, 0, 0) #black
    draw_ellipse(200, 200, 100, 550)

    #draw face
    set_fill_color(0, 1, 0) #green
    draw_ellipse(200, 200, 100, 200) #face outline
    #draw mouth
    set_stroke_color(1, 0, 0) #red lipstick
    set_fill_color(1, 0, 1) #pink
    draw_circle(200, 270, 55)
    #draw eyes
    set_stroke_color(0, 0, 0) #black eyeliner
    draw_line(130, 85, 170, 120)
    draw_line(270, 85, 230, 120)
    draw_line(131, 87, 171, 122)
    draw_line(269, 87, 229, 122)
    draw_line(132, 89, 172, 124)
    draw_line(268, 89, 228, 124)
    draw_line(133, 91, 173, 126)
    draw_line(267, 91, 227, 126)
    draw_line(134, 93, 174, 128)
    draw_line(266, 93, 226, 128)
    draw_line(135, 95, 175, 130)
    draw_line(265, 95, 225, 130)
    #thick eyeliner

    #parameter
    x = 230
    y = 300

    #draw mic
    set_fill_color(0, 0, 0) #black
    draw_rectangle(x - 48, y - 50, 46, 280)
    draw_circle(x - 25, y - 50, 23)
    set_stroke_color(1, 0, 1) #pink
    draw_line(x - 25, y - 73, x - 25, y - 50)
    draw_line(x - 48, y - 50, x - 2, y - 50)

    #draw arm and hand
    set_stroke_color(0, 0, 0) #black
    set_fill_color(1, 1, 1) #white
    draw_rectangle(x, y, 300, 50) #draw arm
    draw_rectangle(x - 50, y - 10, 50, 70) #draw hand

    #draw bangs
    set_fill_color(0, 0, 0) #black
    draw_rectangle(120, 1, 160, 80)

    #draw earrings
    set_stroke_color(1, 1, 0) #yellow
    set_fill_color(1, 1, 0) #yellow
    draw_triangle(100, 200, 70, 280, 130, 280) #left earring
    draw_triangle(300, 200, 270, 280, 330, 280) #right earring

    #my name
    set_stroke_color(0, 0, 0) #black
    draw_text("Minh T. Nguyen", 7, 380)

start_graphics(mydraw) #Special note: pass the name of the main draw function