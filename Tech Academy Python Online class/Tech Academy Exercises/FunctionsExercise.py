#python version 2.7.14
# Author: Dustin Vandehey

#This program will demonstrate how to pass a variable from function to function while producing a functional game.

def start():
    f_name="Sarah"
    l_name="Connor"
    age=28
    gender="Female"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("Hello my name is {}{}, and I am a {} year old {}".format(f_name,l_name, age, gender))











if __name__ == "__main__":
    start()
