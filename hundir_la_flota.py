
import os
import sys
sys.stdout = open(os.devnull, "w")
from hundir_la_flota_funciones import *
from hundir_la_flota_variables import *
import numpy as np
import random
from emoji import emojize
import pygame
sys.stdout = sys.__stdout__
import pandas as pd
from time import sleep

pygame.init()
pygame.mixer.init()


# Welcome to the player
print("Welcome to the Battleship game \n")
username = "machine"
username = input("Please enter your username: ")
print("\nHello" , username , ", now you can place your boats  \n")
sleep(1)


# # We start all the boards
board_machine = board_starter()
board_user = board_starter()
board_shooting_user = board_starter()
board_shooting_machine = board_user

# Ask the user to place his boats
print("This is your board  \n")
sleep(1)
print(pd.DataFrame(board_user, columns=list('          ')), "\n")
sleep(1)
place_all_boats(board_user, available_boats_list_user, boat_position_list_user)
sleep(1)
print("Thanks for placing your boats  \n")
sleep(1)

# We place the random boats for the machine
print("Placing machine boats  \n")
sleep(1)
place_all_boats_random(board_machine, available_boats_list_machine, boat_position_list_machine)
print("Machine boats have been placed  \n")
sleep(1)

# Place special character 
sleep(1)
print("\nSuper octopus being placed. If you shoot the octopus, it will shoot to all its edges  \n")
place_octopus(board_machine)
place_octopus(board_user)
sleep(1)
print("This is your board \n")
sleep(1)
print(pd.DataFrame(board_user, columns=list('          ')), "\n")
sleep(1)
print("Now the real game starts  \n")
sleep(1)

# Here we are going to define the shooting
while True:
    print("Your turn  \n")
    sleep(1)
    print(pd.DataFrame(board_shooting_user, columns=list('          ')), "\n")
    sleep(1)
    shooting_user(board_machine, board_shooting_user)
    if "\U000026F5" not in board_machine:
        print("\nUser wins  \n")
        break
    print("\nMachine's turn  \n")
    shooting_random(board_user, board_shooting_machine)
    if "\U000026F5" not in board_user:
        print("Machine wins  \n")
        break



