import numpy as np
import random
import os
import pygame
from emoji import emojize
import pandas as pd
from time import sleep
from hundir_la_flota_variables import *


# SOUND FUNCTIONS

def play_boat_sound():
    '''
    This function plays the sound for a boat shoot
    '''
    pygame.mixer.Sound.play(pygame.mixer.Sound("boat_sound.wav"))


def play_water_sound():
    '''
    This function plays the sound for a water shoot
    '''
    pygame.mixer.Sound.play(pygame.mixer.Sound("water_sound.wav"))
    

def play_octopus_sound():
    '''
    This functions plays the sound for an octopus shoot
    '''
    pygame.mixer.Sound.play(pygame.mixer.Sound("octopus_sound.wav"))



# BOARD ELEMENTS FUNCTIONS

def board_starter():
    '''
    This function defines the initial empty board, filled with a white circle emoji, and returns the board
    '''
    board = np.full((10,10), fill_value=water_icon)
    return board


def place_octopus(board):
    '''
    This function places the octopus in a random position on the board
    If in the chosen position there is a boat, it will choose another random one
    '''
    octopus_positioned = False
    while octopus_positioned == False:
        octopus_column = random.randint(0, 9)
        octopus_row = random.randint(0, 9)
        octopus_position = (octopus_row, octopus_column)
        if board[octopus_position] != boat_icon:
            board[octopus_position] = octopus_icon
            octopus_positioned = True


def choose_boat_manual(available_boats_list):
    '''
    This functions allows the user to choose the boats to place manually, and it returns the chosen boat
    It will show all the available boats with their indexes, and let the user enter the index of the boat to place.
    '''
    sleep(1)

    # This loop prints every available boat with its index
    for available_boat_index, available_boat in enumerate(available_boats_list):
        print(available_boat_index, available_boat)

    sleep(1)

    # This loop requests and index to the user, from 0 to 9
    # If the entered number is smaller than 0 or bigger than 10 it will request a new number
    chosen_boat_index = int(input("\nEnter the number of the boat you want to place: "))
    while 0 > chosen_boat_index or chosen_boat_index > 9:
        chosen_boat_index = int(input("\nWrong number, enter a valid number: "))

    # Here we define the chosen boat as the element of the previous list which corresponds
    # to the index chosen by the user. Once define, we remove the chosen boat from the
    # available boats list
    chosen_boat_manual = available_boats_list[chosen_boat_index]
    available_boats_list.pop(chosen_boat_index)
    sleep(1)
    print("\nYou chose the boat:" , chosen_boat_manual, "\n")
    return chosen_boat_manual


def choose_boat_random(available_boats_list):
    '''
    This function randomly chooses a boat from the list of available boats list, and it returns the chosen boat
    It will show all the available boats with their indexes, and let the user enter the index of the boat to place.
    '''

    # We define that, if there is just one boat in the list, the chosen index will be 0
    # We identify the boat, remove it from the available boats list and return the chosen boat
    if len(available_boats_list) == 1:
        chosen_boat_random = available_boats_list[0]
        available_boats_list.pop(0)
        return chosen_boat_random

    # If there's more than one element in the list, we will generate a random number between 0 and the number of elements
    # in the list minus 1. The boat is identified and removed from the available boat list, returning the chosen boat
    else:
        index = random.randint(0,(len(available_boats_list)-1))
        chosen_boat_random = available_boats_list[index]
        available_boats_list.pop(index)
    return chosen_boat_random
    

def define_starting_position_coordenates_manual(board,chosen_boat_manual):
    '''
    This function lets the user define the starting coordenates of the chosen boat
    '''
    # We convert the chosen boat variable into its size
    # We create a variable which set the position as not defined
    chosen_boat_manual = len(str(chosen_boat_manual))
    starting_position_defined_manual = False

    # This loop will continue until the starting position will be defined
    while starting_position_defined_manual == False:
        sleep(1)
        # We request the user to enter the starting position column number
        starting_column_manual = int(input("Enter the number of the starting position column: "))

        # This loop will start if the user enters a number below 0 or over 10 and will request a new number
        while 0 > starting_column_manual or starting_column_manual > 10:
            starting_column_manual = int(input("\nWrong number, enter a number from 0 to 9"))

        # We request the user to enter the starting position row number
        starting_row_manual = int(input("\nEnter the number of the starting position row: "))

        # This loop will start if the user enters a number below 0 or over 10 and will request a new number
        while 0 > starting_row_manual or starting_row_manual > 10:
            starting_row_manual = int(input("\nWrong number, enter a number from 0 to 9"))

        # We define the starting position coordenates as the entered row and column
        boat_starting_position_manual = (starting_row_manual, starting_column_manual)
        sleep(1)
        print("\nThe starting position is:" , boat_starting_position_manual, "\n")

        # This will checked if there is a boat in the starting position
        # If there is, the original loop will continue requesting new elements
        # If not, the boat will be placed
        if board[boat_starting_position_manual] != boat_icon:
            starting_position_defined_manual = True
        else:
            print("There is already a boat in this cell, please pick a different one \n")

    return boat_starting_position_manual, starting_column_manual, starting_row_manual


# FUNCION DEFINIR COORDENADAS BARCO INDIVIDUAL RANDOM

def define_boat_position_random(board,chosen_boat_random):

    chosen_boat_random = len(str(chosen_boat_random))
    position_defined = False

    while position_defined == False:
        column = random.randint(0, 9)
        while 0 > column or column > 10:
            column = random.randint(0, 9)
        row = random.randint(0, 9)
        while 0 > row or row > 10:
            row = random.randint(0, 9)
        boat_position = (row, column)
        if board[boat_position] != "\U000026F5":
            position_defined = True
    return boat_position,column,row


# FUNCION PEDIR DIRECCIÓN BARCO INDIVIDUAL AL USUARIO

def choose_direction(board,chosen_boat_manual):

    boat_starting_position_manual, starting_column_manual, starting_row_manual = define_starting_position_coordenates_manual(board,chosen_boat_manual)

    starting_column_manual = int(starting_column_manual)
    starting_row_manual = int(starting_row_manual)
    chosen_boat_manual = len(str(chosen_boat_manual))

    sleep(1)
    if (9 - starting_column_manual) < chosen_boat_manual:
        if (9 - starting_row_manual) < chosen_boat_manual:
            print("Available positions: North or West \n")
            sleep(1)
            direction = input("Enter N for North or W for West: ")
        elif (starting_row_manual) < chosen_boat_manual: 
            print("Available positions: South or West \n")
            sleep(1)
            direction = input("Enter S for South or W for West: ")
        else:
            print("Available positions: North, South or West \n")
            sleep(1)
            direction = input("Enter N for North, S for South or W for West: ")
    elif (starting_column_manual) < chosen_boat_manual:
        if (starting_row_manual) < chosen_boat_manual:
            print("Available positions: South or East \n")
            sleep(1)
            direction = input("Enter S for South or E for East: ")
        elif (9 - starting_row_manual) < chosen_boat_manual:
            print("Available positions: North or West \n")
            sleep(1)
            direction = input("Enter N for North or W for West: ")
        else: 
            print("Available positions: North, South or East \n")
            sleep(1)
            direction = input("Enter N for North, S for South or E for East: ")
    elif (9 - starting_row_manual) < chosen_boat_manual: 
        print("Available positions: North or West \n")
        sleep(1)
        direction = input("Enter N for North, E for East or W for West: ")
    elif (starting_row_manual) < chosen_boat_manual: 
            print("Available positions: South, East or West \n")
            sleep(1)
            direction = input("Enter S for South, E for East or W for West: ")
    else:
        print("Available positions: North, South, East or West \n")
        sleep(1)
        direction = input("Enter N for North, S for South, E for East or W for West: ")
        

    return direction, boat_starting_position_manual, starting_column_manual, starting_row_manual


# FUNCIÓN DEFINIR DIRECCIÓN RANDOM

def choose_direction_random(board,chosen_boat_random):

    boat_position,column,row = define_boat_position_random(board,chosen_boat_random)

    column = int(column)
    row = int(row)
    chosen_boat_random = len(str(chosen_boat_random))

    direction_list = ["North", "South", "East", "West"]

    if (9 - column) < chosen_boat_random:
        if (9 - row) < chosen_boat_random:
            direction_list.remove("South")
            direction_list.remove("East")
            direction = random.choice(direction_list)
        elif (row) < chosen_boat_random: 
            direction_list.remove("North")
            direction_list.remove("East")
            direction = random.choice(direction_list)
        else:
            direction_list.remove("East")
            direction = random.choice(direction_list)
    elif (column) < chosen_boat_random:
        if (row) < chosen_boat_random:
            direction_list.remove("North")
            direction_list.remove("West")
            direction = random.choice(direction_list)
        elif (9 - row) < chosen_boat_random:
            direction_list.remove("South")
            direction_list.remove("East")
            direction = random.choice(direction_list)
        else: 
            direction_list.remove("West")
            direction = random.choice(direction_list)
    elif (9 - row) < chosen_boat_random: 
        direction_list.remove("South")
        direction = random.choice(direction_list)
    elif (row) < chosen_boat_random: 
        direction_list.remove("North")
        direction = random.choice(direction_list)
    else:
        direction = random.choice(direction_list)

    return direction, boat_position, column, row


# FUNCION COLOCAR BARCO INDIVIDUAL

def place_single_boat(board,chosen_boat_manual,boat_position_list):

    direction, boat_starting_position_manual, starting_column_manual, starting_row_manual = choose_direction(board,chosen_boat_manual)

    boat_starting_position_manual = [(boat_starting_position_manual)]
    starting_column_manual = int(starting_column_manual)
    starting_row_manual = int(starting_row_manual)
    chosen_boat_manual = len(str(chosen_boat_manual))

    sleep(1)
    print("\nPlacing boat in direction" , direction, "and position" , boat_starting_position_manual, "\n")

    while len(boat_starting_position_manual) < chosen_boat_manual:
    
        if direction == "N":
            starting_row_manual = starting_row_manual - 1
        elif direction == "S":
            starting_row_manual = starting_row_manual + 1
        elif direction == "E":
            starting_column_manual = starting_column_manual + 1
        elif direction == "W":
            starting_column_manual = starting_column_manual - 1

        boat_starting_position_manual.append((starting_row_manual, starting_column_manual))

    for elem in boat_starting_position_manual:
        board[elem] = "\U000026F5"

    sleep(1)
    print(pd.DataFrame(board, columns=list('          ')), "\n")
    sleep(1)
    print("Your boat has been placed \n")
    return board


# FUNCION COLOCAR BARCO MÁQUINA

def place_single_boat_random(board,chosen_boat_random, boat_position_list):
    
    boat_has_been_placed = False

    while boat_has_been_placed == False:
        direction, boat_position, column, row = choose_direction_random(board,chosen_boat_random)
        boat_position = [(boat_position)]
        column = int(column)
        row = int(row)
        chosen_boat_random = len(str(chosen_boat_random))

        while len(boat_position) < chosen_boat_random:
        
            if direction == "North":
                row = row - 1
            elif direction == "South":
                row = row + 1
            elif direction == "East":
                column = column + 1
            elif direction == "West":
                column = column - 1

            boat_position.append((row, column))

        for elem in boat_position:
            if elem in boat_position_list:
                boat_position.pop[0]
        if len(boat_position) == chosen_boat_random:
            boat_position_list.append(boat_position)
            for elem in boat_position:
                board[elem] = "\U000026F5"
            boat_has_been_placed = True
    return board


# FUNCION COLOCAR TODOS LOS BARCOS

def place_all_boats(board, available_boats,boat_position_list):
    sleep(1)
    print("Would you like to place your boats manually or random? \n")
    sleep(1)
    manual_or_random = input("Enter M for manually or R for random: ")
    if manual_or_random == "M":
        while len(available_boats) > 0:
            chosen_boat_manual = choose_boat_manual(available_boats)
            place_single_boat(board, chosen_boat_manual, boat_position_list)
    elif manual_or_random == "R":
        place_all_boats_random(board,available_boats, boat_position_list)
        print("\nPlacing your boats \n")
        sleep(1)
        print(pd.DataFrame(board, columns=list('          ')), "\n")

# FUNCION COLOCAR TODOS LOS BARCOS RANDOM

def place_all_boats_random(board, available_boats, boat_position_list):
    while len(available_boats) > 0:
        chosen_boat_random = choose_boat_random(available_boats)
        place_single_boat_random(board, chosen_boat_random, boat_position_list)


# FUNCIÓN SELECCIONAR MODO DE DISPARO

def define_shooting_mode():
    print("Would you like to choose your shooting position or do you want to shoot randomly? \n")
    sleep(1)
    shooting_mode = input("Enter M for manual or R for random: ")
    sleep(1)
    return shooting_mode

# FUNCIÓN SELECCIONAR POSICIÓN DISPARO

def define_shooting_target(board):
    target_row = int(input("\nEnter the row where you want to shoot: "))
    target_column = int(input("\nEnter the column where you want to shoot: "))
    target = (target_row, target_column)
    target_octopus = [(target)]
    print(board[target], "\n")
    return target, target_octopus, target_row, target_column

# FUNCIÓN SELECCIONAR POSICIÓN DISPARO RANDOM

def define_shooting_target_random(board):
    target_row = random.randint(0, 9)
    target_column = random.randint(0, 9)
    target = (target_row, target_column)
    target_octopus = [(target)]
    return target, target_octopus, target_row, target_column


# FUNCIÓN RESULTADO DISPARO TOUCHED
def result_shoot_touched(board,board_shooting,target):
    print("Touched \n")
    play_boat_sound()
    board_shooting[target] = "\U0000274C"
    board[target] = "\U0000274C"
    print(pd.DataFrame(board_shooting, columns=list('          ')), "\n")
    return board, board_shooting


# FUNCIÓN RESULTADO DISPARO PULPO
def result_shoot_octopus(board,board_shooting,target_row,target_column,target_octopus):
    print("Octopus \n")
    play_octopus_sound()
    if target_row == 0 and target_column == 0:
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))

    elif target_row == 9 and target_column == 0:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))

    elif target_row == 9 and target_column == 9:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))

    elif target_row == 0 and target_column == 9:
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
    elif target_row == 0:
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
    elif target_row == 9:
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
    elif target_column == 0:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
    elif target_column == 9:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
    else:
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_column = target_column - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_column = target_column + 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
        target_row = target_row - 1
        target_octopus.append((target_row,target_column))
    for elem in target_octopus:
        board_shooting[elem] = "\U0000274C"
        board[elem] = "\U0000274C"
    print(pd.DataFrame(board_shooting, columns=list('          ')), "\n")
    return board, board_shooting


# FUNCIÓN RESULTADO DISPARO AGUA
def result_shoot_water(board, board_shooting, target):
    print("Water \n")
    play_water_sound()
    board_shooting[target] = "\U0001F300"
    board[target] = "\U0001F300"
    print(pd.DataFrame(board_shooting, columns=list('          ')), "\n")
    water = True
    return board, board_shooting, water

# FUNCION DISPAROS USUARIO

def shooting_user(board, board_shooting):

    shooting_mode = define_shooting_mode()
    if shooting_mode == "M":
        water = False

        while water == False:
            if "\U000026F5" in board:
                sleep(1)
                target, target_octopus, target_row, target_column = define_shooting_target(board)

                if board[target] != "\U0000274C" and board[target] != "\U0001F300":

                    if board[target] == "\U000026F5":
                        board, board_shooting = result_shoot_touched(board,board_shooting,target)

                    elif board[target] == "\U0001F419":
                        board, board_shooting = result_shoot_octopus(board,board_shooting,target_row,target_column,target_octopus)
                    else:
                        board, board_shooting, water = result_shoot_water(board, board_shooting, target)
                else:
                    print("You have already shoot to this position, please choose your cell again, \n")
            else:
                water = True
    if shooting_mode == "R":
            shooting_random(board, board_shooting)
    
    return board, board_shooting


# FUNCION DISPAROS MAQUINA

def shooting_random(board,board_shooting):

    water = False

    while water == False:
        if "\U000026F5" in board:
            sleep(1)
            target, target_octopus, target_row, target_column = define_shooting_target_random(board)

            if board[target] != "\U0000274C" and board[target] != "\U0001F300":
                if board[target] == "\U000026F5":
                    board, board_shooting = result_shoot_touched(board,board_shooting,target)

                elif board[target] == "\U0001F419":
                    board, board_shooting = result_shoot_octopus(board,board_shooting,target_row,target_column,target_octopus)

                else:
                    board, board_shooting, water = result_shoot_water(board, board_shooting, target)
        else:
            water = True

        return board, board_shooting