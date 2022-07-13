import random
import numpy as np

NUM_OF_SIMS = 100000

def __init__():
    num_players = repl() #get num players from user
    wins = np.zeros(num_players, dtype=int) #an array to count number of wins by each player
    time = 0 
    for _ in range(NUM_OF_SIMS): #run a game NUM_OF_SIMS times
        game = Game(num_players)
        winner = game.run() #gets player position of the winner
        wins[winner] += 1 
        time += 1
        if time % 10000 == 0:
            print(time)
    for i in range(len(wins)):
        print("Player " + str(i + 1) + " wins: " + str(wins[i] / NUM_OF_SIMS)) #prints percent of time each player wins


def repl():
    done = False
    while done == False:
        num_players = int(input("How many players are there? (20 max) \n"))
        if num_players > 1 and num_players <= 20: #make sure player num is between 1 and 20
            done = True
        else:
            print("invalid input, please enter a number between 1 and 20!")
    return num_players

class Game():
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = np.zeros(num_players, dtype=int) #an array to represent each player as an int of their number of bills
        self.players += 3 #start each player with 3 bills

    def run(self):
        turn = 0 #counter to track position in array of whose turn it is
        while not self.is_over(): #while at least 2 players have bills
            num_die = self.players[turn]
            if num_die > 3: #determine number of die (max is 3) based on bills
                num_die = 3
            for _ in range(num_die):
                roll = random.randint(1,6)
                if roll < 4: #for 4,5,6 do nothing
                    self.players[turn] -= 1 #lose a bill whether to left right or center
                    if roll == 1: #pass to left on 1
                        if turn == 0: #shift left in array unless entry 0 in which case pass to end
                            self.players[len(self.players) - 1] += 1
                        else:
                            self.players[turn - 1] += 1
                    if roll == 2: #pass to right on 2
                        if turn == len(self.players) - 1: #shift right in array unless last entry in which case pass to start
                            self.players[0] += 1
                        else:
                            self.players[turn + 1] += 1
                    #note it passes center for 3 just no additional code is needed

            #advance the turn (reseting to position 0 if at end of cycle)               
            if turn == len(self.players) - 1:
                turn = 0
            else:
                turn += 1
        
        #now return winner's position
        for i in range(len(self.players)):
            if not self.players[i] == 0:
                return i

    def is_over(self):
        num_left = 0
        for i in range(len(self.players)):
            if not self.players[i] == 0:
                num_left += 1
        return num_left == 1 #if only one player has bills, game is over

if __name__ == "__main__":
    __init__()