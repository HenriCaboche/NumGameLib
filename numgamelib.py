import kandinsky
import time

# Placeholder :
fps = 60
## Creates moving objects
def create_active(pos_x_o=int, pos_y_o=int,height=int,width=int,velocity_x=int,velocity_y=int,colour=any,backround_col=any,upper_limit_x=int):
    velocity_x= velocity_x
    velocity_y =velocity_y
    pos_x=pos_x_o
    pos_y=pos_y_o
    while True:
      # Path handler
        if pos_x > upper_limit_x or pos_x < pos_x_o:
            print("a")
            velocity_x= -1*velocity_x
            velocity_y= -1*velocity_y
            pos_x+=velocity_x
            pos_y+=velocity_y
          # Movement handler
        else:
            kandinsky.fill_rect(pos_x,pos_y,width,height,colour)
            time.sleep(1/fps)
            kandinsky.fill_rect(pos_x,pos_y,width,height, backround_col)
            pos_x+=pos_x+velocity_x
            pos_y+=velocity_y
## Creates gravity
def gravity(velocityY,gravityStrenght):
    velocityY -= 1 * gravityStrenght

## Creates player objects
def create_player(pos_x_o=int, pos_y_o=int,height=int,width=int,velocity_x=int,velocity_y=int,colour=any,backround_col=any,isGravity=bool,playerGravityStrenght=int):
    velocity_x= velocity_x
    velocity_y =velocity_y
    if isGravity:
        gravity(playerGravityStrenght)
    pos_x=pos_x_o
    pos_y=pos_y_o
    # Main loop
    while True:
        kandinsky.fill_rect(pos_x,pos_y,width,height,colour)
        if ion.keydown(ion.KEY_LEFT):
            # Screen refresh
            kandinsky.fill_rect(pos_x,pos_y,width,height, backround_col)
            # Input handler
            pos_x-= velocity_x
        elif ion.keydown(ion.KEY_RIGHT):
            kandinsky.fill_rect(pos_x,pos_y,width,height, backround_col)
            pos_x+= velocity_x
        elif ion.keydown(ion.KEY_UP):
            kandinsky.fill_rect(pos_x,pos_y,width,height, backround_col)
            pos_y-= velocity_y
        elif ion.keydown(ion.KEY_DOWN):
            kandinsky.fill_rect(pos_x,pos_y,width,height, backround_col)
            pos_y+= velocity_y
def create_object (posX=int,posY=int,Width=int,Height=int,color=any):
    kandinsky.fill_rect(posX,posY,Width,Height,color)