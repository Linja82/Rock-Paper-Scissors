"""
Rock Paper Scissors V1
@date June 11, 2020 5:04 PM
@author Linja
"""

import sys
import time
import random
import pygame

pygame.init()

# Graphics
rock = pygame.image.load("Assets/Rock-1.png")
paper = pygame.image.load("Assets/Paper-1.png")
scissors = pygame.image.load("Assets/Scissors-1.png")
background = pygame.image.load("Assets/Background 0.png")
icon = pygame.image.load("Assets/Icon.png")

# Fonts
labelFont_32 = pygame.font.Font('impact.ttf', 32)
labelFont_40 = pygame.font.Font('impact.ttf', 40)

# Colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Variables
window_size = (650, 650)
player_score = 0
player_score_text = "Score: " + str(player_score)
computer_score = 0
computer_score_text = "Score: " + str(computer_score)
selection = ""

# Booleans
state = True

# Initialization Code
window = pygame.display.set_mode(window_size)                   # Creates a window and stores it in a variable
pygame.display.set_caption("Rock Paper Scissors")
pygame.display.set_icon(icon)


# Functions
def draw(item, x, y):
    window.blit(item, (x, y))


def impact_32(text, colour, x, y):                              # Creates text with font impact size 32 at position x, y
    label = labelFont_32.render(text, True, colour)
    draw(label, x, y)


def impact_40(text, colour, x, y):                              # Creates text with font impact size 40 at position x, y
    label = labelFont_40.render(text, True, colour)
    draw(label, x, y)


def is_win(selection_3, opponent):
    if selection_3 == "Rock" and opponent == 0:
        return "Tie"
    elif selection_3 == "Rock" and opponent == 1:
        return "Loss"
    elif selection_3 == "Rock" and opponent == 2:
        return "Win"
    elif selection_3 == "Paper" and opponent == 0:
        return "Win"
    elif selection_3 == "Paper" and opponent == 1:
        return "Tie"
    elif selection_3 == "Paper" and opponent == 2:
        return "Loss"
    elif selection_3 == "Scissors" and opponent == 0:
        return "Loss"
    elif selection_3 == "Scissors" and opponent == 1:
        return "Win"
    elif selection_3 == "Scissors" and opponent == 2:
        return "Tie"


def game(selection_2):
    if selection_2 == "Rock":
        draw(rock, 100, 280)
    elif selection_2 == "Paper":
        draw(paper, 100, 280)
    elif selection_2 == "Scissor":
        draw(scissors, 100, 280)
    opponent = random.randint(0, 2)                             # Generates opponent move 0: Rock, 1: Paper, 2: Scissors
    if opponent == 0 and selection_2 != "":
        draw(rock, 430, 280)
    elif opponent == 1 and selection_2 != "":
        draw(paper, 430, 280)
    elif opponent == 2 and selection_2 != "":
        draw(scissors, 430, 280)
    result = is_win(selection_2, opponent)
    if result == "Win":
        global player_score
        player_score += 1
    elif result == "Loss":
        global computer_score
        computer_score += 1


# Start Screen
while state:
    for event in pygame.event.get():                            # Captures all in window events
        if event.type == pygame.QUIT:                           # If event is of exit type
            sys.exit()                                          # Exit the program
        if event.type == pygame.KEYDOWN:                        # If event is of key down type
            if event.key == pygame.K_RETURN:                    # If the key down is "ENTER"
                state = False                                   # Exits the start screen

    draw(background, 0, 0)                                      # Draws the background
    impact_40("Welcome to Rock Paper Scissors", WHITE, 59, 80)  # Draws welcome text
    draw(rock, 73, 220)                                         # Draws the rock icon
    draw(paper, 265, 220)                                       # Draws the paper icon
    draw(scissors, 457, 220)                                    # Draws the scissor icon
    impact_32("Press Enter to start", WHITE, 199, 450)          # Draws start instructions

    pygame.display.update()                                     # Updates the window

# Main While Loop | The actual game is here
while True:
    selection = ""
    for event in pygame.event.get():                            # Captures all in window events
        if event.type == pygame.QUIT:                           # If event is of exit type
            sys.exit()                                          # Exit the program
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selection = "Rock"
            elif event.key == pygame.K_2:
                selection = "Paper"
            elif event.key == pygame.K_3:
                selection = "Scissor"

    player_score_text = "Score: " + str(player_score)
    computer_score_text = "Score: " + str(computer_score)
    draw(background, 0, 0)                                      # Draws the background
    impact_40("Choose a move", WHITE, 203, 80)
    impact_32("Player 1:", WHITE, 100, 180)
    impact_32(player_score_text, WHITE, 100, 220)
    impact_32("Player 2:", WHITE, 441, 180)
    impact_32(computer_score_text, WHITE, 441, 220)
    impact_32("Controls:", WHITE, 267, 500)
    impact_32("1 = Rock, 2 = Paper, 3 = Scissor", WHITE, 130, 550)
    game(selection)

    pygame.display.update()                                     # Updates the window
    time.sleep(1)
