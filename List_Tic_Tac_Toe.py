'''#----------------Text Based Version of Tic Tac Toe-------------------------

#First step, break down problem into small pieces, and tackle each problem

#We need some sort of game map, a way to visualize Tic Tac Toe

#Let's keep this simple. We'll be working with 0's 1's and 2's 

#We're going to be using a lists, of lists to organize.

game = (0,0,0,
        0,0,0,
        0,0,0)

#There's an issue with this Tic Tac Toe map, when printed onto the console it just prints out a string of zeros.. not in a tic tac tow shape.
#game is also a Tuple, which makes it harder to change
print(game)

#So what we're going to do is change the tuple to a LIST by changing the parentheses (()) to brackets ([])


game2 = [0,0,0,
        0,0,0,
        0,0,0]

print(game2)

#Now we have a list, BUT it still comes out as a straight across zeros... What we can do is make a list of list

game3 = [[0,0,0],
        [0,0,0],
        [0,0,0]]

print(game3)

#Still not printing out right so we can just iterate over the game to print it out right

for line in game3:
    print(line)
    

#----------------Built-In Functions-------------------------
#How are we going to represent the tic tac toe board
# We want to add a print stateemnet before the print row

#This takes care of the top row, how do we take care of the column
print(" 0  1  2")
for line in game3:
    print(line)

#For this we could use a counter
print("   0  1  2")
count = 0
for line in game3:
    print(count, line)

#Now we got the numbers to show up BUT we want count to be a countdown

print("   0  1  2")
count = 0
for line in game3:
    print(count, line)
    count += 1 # OR count = count+1

#we'll be using the built-in function of Enumerate
print("   0  1  2")
for count, line in enumerate(game3):
    print(count, line)
    triple line comment 
    for item in line:
        print(item)

#we'll be using the built-in function of Enumerate
print("   a  b  c")
for count, line in enumerate(game3):
    print(count, line)
    #This would be a for loop within a for loop to go through all the values in a matrix
    triple line comment 
    for item in line:
        print(item)


#----------------Indexes with list/ Slices-------------------------
#This is just an exmple:
l = [1,2,3,4,5]

#To access an element within the list - this should give us '2'
print(l[1])

#To access the last element within in the list - this should give us '5'
print(l[-1])

#Referencing a slice
print(l[1:3])

#Set something at a specific index
l[1] = 99

print(l)

#----back to the game
#Making a change within game
game_final = [[0,0,0],
            [0,0,0],
            [0,0,0]]

game_final[0][1] = 1

print("   a  b  c")
for count, line in enumerate(game_final):
    print(count, line)

#----------------Functions-------------------------
#anytime you have repition - use a funtion - or a loop

game_final = [[0,0,0],
            [0,0,0],
            [0,0,0]]

#this function just prints

def game_board():
    print("   a  b  c")
    for count, line in enumerate(game_final):
        print(count, line)

#Running this function
game_board()

game_final[0][1] = 1

game_board()

#take input from the user 


#----------------Functions: Parameters and Typing-------------------------
#some exapmles with functions with parameters
def add(x,y):
    return x+y

z=add("hey"," there")
print(z)'''


#back to the gameboard example

game_final = [[0,0,0],
            [0,0,0],
            [0,0,0]]

#We need to pass parametesrs throught this function:
#You can set your function to default numbers, player=0, row=0, and column=0
def game_board(player=0, row=0, column=0, just_display=False):
    print("   a  b  c")

    if not just_display:
        game_final[row][column] = player

    for count, line in enumerate(game_final):
        print(count, line)

#Running this function
current_player = 1
row_choice = 2
col_choice = 0
game_board(just_display=True)
game_board(current_player , row_choice, col_choice)

#----------------Mutability Revisited-------------------------

