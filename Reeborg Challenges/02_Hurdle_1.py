def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Method 1:For Loop
for i in range(6):
    jump()

# Method 2: While Loop
while not at_goal():
    jump()