#!/usr/bin/env python
# coding: utf-8

# In[49]:


#For computer randomization
import random

#Constants
head = ('''
 __     __
|  |   |  |
|  |___|  |
|   ___   |
|  |   |  |
|__|   |__|
''')


tail = ('''
 __________
|___    ___|
    |  |
    |  |
    |  |
    |__|
''')

#Begin the gaime
play_again = ("")
games = 0
win = 0
lost = 0

print("Welcome to the classic \"head or tail\"!")

while play_again not in ("N", "n"):

    #starting a while loop for player input validation
    player_choose = ("")
    while player_choose not in ("head", "tail"):
        player_choose = input("Please choose by typing \"head\" or \"tail\"! ").lower()

    #printing player's choic:
    print("You choose:")
    if player_choose == "head":
        print(head)
    else:
        print(tail)

    #Randomize computer's choice:
    rand_num = random.randint(0,1)
    if rand_num == 0:
        result = head
    else:
        result = tail

    #Printing compiuter's choice:
    print("The result is:")
    print(result)

    #Checking the result and the player's choice:
    if player_choose == "head" and result == head:
        print("You win!")
        win += 1
        games += 1
    elif player_choose == "tail" and result == tail:
        print("You win!")
        win += 1
        games += 1
    else:
        print("You lost!")
        lost += 1
        games += 1
        
    #validate the user input for play_again    
    play_again = ("")
    while play_again not in ("Y", "y", "N", "n"):
        play_again = input("Play again? Y/N: ")
    
#Print out the result summary according to how many games the user have played and the wins and losses. 
if games == 1:
    print(f"You have played {games} game. You have won {win} time, and lost {lost} time.")
else:
    if win == 1 and lost == 1:
        print(f"You have played {games} games. You have won {win} time, and lost {lost} time.")
    elif win > 1 and lost > 1:
        print(f"You have played {games} games. You have won {win} times, and lost {lost} times.")
    elif win == 1 and lost > 1:
        print(f"You have played {games} games. You have won {win} time, and lost {lost} times.")
    elif win > 1 and lost == 1:
        print(f"You have played {games} games. You have won {win} times, and lost {lost} time.")
    elif win > 1 and lost == 0:
        print(f"You have played {games} games. You have won {win} times, and lost {lost} time.")
    elif win == 0 and lost > 1:
        print(f"You have played {games} games. You have won {win} time, and lost {lost} times.")


# In[ ]:




