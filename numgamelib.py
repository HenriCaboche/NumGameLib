## creates moving objects
def create_active(pos_x_o=int, pos_y_o=int,height=int,width=int,velocity_x=int,velocity_y=int,colour=any,backround_col=any,upper_limit_x=int):
    velocity_x= velocity_x
    velocity_y =velocity_y
    pos_x=pos_x_o
    pos_y=pos_y_o
    while True:
      #path handler
        if pos_x > upper_limit_x or pos_x < pos_x_o:
            print("a")
            velocity_x= -1*velocity_x
            velocity_y= -1*velocity_y
            pos_x+=velocity_x
            pos_y+=velocity_y
          #movement handler
        else:
            kandinsky.fill_rect(pos_x,pos_y,width,height,colour)
            time.sleep(1/fps)
            kandinsky.fill_rect(pos_x,pos_y,width,height, backround_col)
            pos_x+=pos_x+velocity_x
            pos_y+=velocity_y
