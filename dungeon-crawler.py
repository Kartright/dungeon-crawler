def movement(direction):
    if direction == 'right':
        print('You move right.')
    elif direction == 'left':
        print('You move left.')
    elif direction == 'forward':
        print('You move forward')
    elif direction == 'backward':
        print('You move backward')
    else:
        print('Please input Right, Left, Forward, or Backward...')
        

print('Welcome to treasure finder. You will be asked to input 8 directions.\nYour options are right, left, forward, and backward.')

direction1 = input("Input a direction: ")
movement(direction1)
direction2 = input("Input a direction: ")
movement(direction2)

if direction1 == 'forward' and direction2 == 'forward':
    print('Great start! Keep going!!')
        
    direction3 = input("Input a direction: ")
    movement(direction3)
    direction4 = input("Input a direction: ")
    movement(direction4)

    if direction3 == 'backward' and direction4 == 'backward':
        print('You are on the right track! Keep it up!')
        
        direction5 = input("Input a direction: ")
        movement(direction5)
        direction6 = input("Input a direction: ")
        movement(direction6)

        if direction5 == 'left' and direction6 == 'right':
            print('Almost there!! Dont stop now!!')
        
            direction7 = input("Input a direction: ")
            movement(direction7)
            direction8 = input("Input a direction: ")
            movement(direction8)

            if direction7 == 'left' and direction8 == 'right':
                print('You found the treasure! Way to go champ!!')
            else:
                print('Ooooh you were so close, but unfortunately you tripped on a branch and broke your leg... and starved to death...')
        
        else:
            print('Oops! You got shot by a booby trap arrow...')
        
    else:
        print('Uh Oh! You ran into a zombie and he ate your brains... maybe try again??')
else:
    print("Sorry. You fell in a pit of snakes and died. Maybe next time...")
