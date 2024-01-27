def turn_right():
    turn_left()
    turn_left()
    turn_left()


def what_to_do():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        turn_left()
    else:
        turn_right()
        move()
        
        
        
what_to_do()
while not at_goal():
    what_to_do()
