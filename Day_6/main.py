# print("Hello")

# ! Python functions and Karel

# def my_function():                      #* def my_function():
#     print("Hello")                      #*     #do this
#     print("Bye")                        #*     #then do this
#                                         #*     #finally do this
# my_function()

# ! While loops                              
# * while something is true:
# *     #do something repeatedly

# ! Reeborg's puzzle 1 & 2
# def move_thrice():
#     move()
#     move()
#     move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def make_square():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
    
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for step in range(6):
#     jump()
    
# while at_goal() != True:
#     jump()

# while not at_goal():
#     jump()

# ! Reeborg hurdle 3
# def move_thrice():
#     move()
#     move()
#     move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def make_square():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
    
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# ! Reeborg hurdle 4
# def move_thrice():
#     move()
#     move()
#     move()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def make_square():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
    
# def jump():
#     turn_left()
#     while not right_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     while front_is_clear():
#         move()
#     turn_left()
    
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# ! Reeborg Maze problem - my code

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
       
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif not right_is_clear() and not front_is_clear():
#         turn_left()
#         turn_left()
#     elif not right_is_clear():
#         move()

# ! Reeborg Maze problem - course code - but needs debugging after day 15

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
