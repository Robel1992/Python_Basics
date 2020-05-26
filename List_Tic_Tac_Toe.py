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
print(z)


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

game_final = "I want to play a game"

#You can check the id of any given element by typing id(element)
print(id(game_final))

def game_board(player=0, row=0, column=0, just_display=False):
    #You can also set game to be a global variable within the function (or outside the function) and the value will be set for it outside the function
    global game_final 
    game_final = "A game"
    print(id(game_final))
    #print(game_final) 
    #you'll notice if you put "print(game_final)" 
    #after the game_final, there is some sort of error. 
    #You wont be able to change the string.. That is becuase 
    #a string is IMMUTABLE. Not able to change.

game_board()
print(game_final)
print(id(game_final))

#Back to playing with the game-------------


game = [1,2,3]

#You can check the id of any given element by typing id(element)
#print(id(game_final))

def game_board(player=0, row=0, column=0, just_display=False):
    #game = "A game" #when you run this, you'll see no change to a 'mutable list' even though lists are 'mutable'
    game[1] = 99
    #print(id(game))
    print(game) 

game_board()
print(game)
#print(id(game_final))

#LESSON LEARNED: You can change elements within the list but you can not change the entire list from the jump.


game_final = [[0,0,0],
            [0,0,0],
            [0,0,0]]

#We need to pass parametesrs throught this function:
#You can set your function to default numbers, player=0, row=0, and column=0
#To prevent any confusion on what id or value of variables being passed, just make a temporary variable to manipulate only in the function: game_map

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print("   a  b  c")
    if not just_display:
        game_map[row][column] = player

    for count, line in enumerate(game_final):
        print(count, line)

    return game_map

#Running this function
game = game_board(game_final, just_display=True)
game = game_board(game_final, player=0,row=2, column=1)

#----------------Error Handling-------------------------
#blank game board
game = [[0,0,0],
            [0,0,0],
            [0,0,0]]


#function to manipulate gameboard
def game_board(game_map, player=0, row=0, column=0, just_display=False):

#When we're testing for the correct input from the user - we'll use a try-except statement: You can pass try:, except:, else:, finally:
#If it is within bounds and the user gives you the right input then you'll put in 
#the correct statement. 
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player

        for count, line in enumerate(game):
            print(count, line)

        #You can throw an error with raise
        raise
        return game_map

#You can put in the actual error you are filtering out for within your ccode.
    except IndexError as e:
        print("Error: Make sure you input row/column as 0 1 or 2?", e)

#You can have multiple exceptions. If you want your code to run indefinitely no matter what collecting data/or parsing the web, you can add another exceptions
    except Exception as e:
        print("Something went very wrong", e)

#You can pass else:
    else:

#You can pass finally:
    #finally count as x
       # print("awesome", x)

#Running this function
game = game_board(game, just_display=True)
game = game_board(game, player=0,row=3, column=1)

#If you pass the wrong arguments in your code // This is just an example
game = game_board(game_board, just_display=True)'''

#----------------Calculating Horizontal Winner-------------------------
#Note: Much easier to finish all the testing without User interface. It's much easier to just have the code play out.
game = [[1,1,1],
        [0,0,0],
        [2,2,0]]

#Ways to win--horizontally--vertically--diagonally

#HARD CODE: Maybe think more dynamic: changing size of column and rows
'''def win(current_game):
    for row in game:
        print(row)
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]

        if col1 == col2 == col3:
            print("Winner!!")

#Very complicated: There is probably some type of function that does this for us. Search on Google.
def win(current_game):
    for row in game:
        print(row)
        all_match = True
        for item in row:
            if item != row[0]:
                all_match = False
        if all_match:
                print("Winner")

#row.count(row[0]) - checks the number of times value comes up in the bitch
#len(row) - is the length of the row
#row[0]!=0 - as long as the first bit of row doesn't equal zero
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0])==len(row) and row[0] != 0:
            #You can print it out with an f""", you can pass a value using {}
            print(f"Player {row[0]} is the winner!")



win(game)'''

#----------------Calculating Horizontal Winner-------------------------