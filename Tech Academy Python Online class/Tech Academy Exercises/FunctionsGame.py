#python version 2.7.14
# Author: Dustin Vandehey

#This program is a game that will demonstrate how to pass a variable from function to function 

def start(nice=0, mean=0, name=""):
    #get user's name
    name=describe_game(name)
    nice,mean,name=nice_mean(nice,mean,name)
def describe_game(name):
    """
    Check if this is a new game or not.
    If it is new, get the users name.
    if it is not, thank the player for
    playing again and continue with the game
    """
    if name!="":# meaning if we do not have this user's name, then they are a new player and we need to get their name.
        print ("\n thank you for playing the game again{}".format(name))
    else:
        stop=True
        while stop:
            if name=="":
                name=raw_input("\nWhat is your name?").capitalize()
                if name!="":
                    print("\nwelcome {}".format(name))
                    print("in this game, you will be greated by several different people. \n you can be nice or mean")
                    print("At the end of the game, your fate will be influenced by your actions.")
                    stop=False
    return name

def nice_mean(nice, mean, name):
    stop=True
    while stop:
        show_score(nice,mean,name)
        pick=raw_input("\nA stranger approaches you for a conversation.\nWill you be nice or mean? n/m:").lower()
        if pick=="n":
            print("They smile, wave, and walk away")
            nice=(nice+1)
            stop=False
        if pick=="m":
            print("\nThe stranger glares at you and storms away")
            mean=(mean+1)
            stop=False
            score(nice,mean,name)#pass the three variable to the score()

def show_score(nice, mean, name):
    print("\n{},You currently have ({}, Nice) and ({} Mean) points.".format(name, nice, mean) )

def score(nice, mean, name):
    #Score function is being passed the value stored within the 3 variables
    if nice>5: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean, name)
    if mean>5: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice, mean, name)
    else:      # call nice_mean function so it can pass in the variables
        nice_mean(nice,mean,nice)
def win(nice, mean, name):
    print("Good job {}. You win and everyone thinks you are nice".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print"Oh no you lse{}. You need to be nicer to people".format(name)
    again(nice,mean,name)

def again(nice, mean, name):
    stop=True
    while stop:
        choice=raw_input("Do you want to play again? y/n").lower()
        if choice=="y":
            stop=False
            reset=(nice,mean,name)
        if choice=="n":
            print ("Bye, thanks for playing")
            stop=False
            exit()
        else:
            print("Please enter y for yes or n for no")

def reset(nice,mean,name):
    nice=0
    mean=0
    start(nice,mean,name)

if __name__ == "__main__":
    start()
