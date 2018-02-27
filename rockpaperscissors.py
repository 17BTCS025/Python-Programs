#Rock, Papers, Scissors simulation
import random

chosen=random.randint(1,3)                        #Randomizing 3 numbers

if chosen==1:                                     #Assigning value to computer
    computer='r'
elif chosen==2:
    computer='p'
else:
    computer=='s'

player=input('Rock(r), Paper(p), Scissor(s)? ')   #User inout for given options
print(player, 'vs' ,computer )

if player==computer:                              #if-else conditions to win/lose
    print('DRAW!')
elif player=='r' and computer=='s':
    print('PLAYER WINS!')
elif player=='r' and computer=='p':
    print('COMPUTER WINS!')
elif player=='s' and computer=='p':
    print('PLAYER WINS!')
elif player=='s' and computer=='r':
    print('COMPUTER WINS!')
elif player=='p' and computer=='r':
    print('PLAYER WINS!')
elif player=='p' and computer=='s':
    print('COMPUTER WINS!')
    


    
