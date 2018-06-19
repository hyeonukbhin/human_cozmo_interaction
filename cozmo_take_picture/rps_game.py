import numpy as np
import random

def main():
    while(1):
        input_user = input("Rock or Paper or Scissor?: ")
        correct_set = ["Rock", "Paper", "Scissor"]
#         print(input_user)
        if input_user in correct_set:
            result = function(input_user)
            print(result)
        else:
            print("not correct")

def function(input_user):
    if input_user == "Rock":
        input_param = 0
    elif input_user == "Paper":
        input_param = 1
    elif input_user == "Scissor":
        input_param = 2

#     input_com = np.random(3)
    com_param = random.randrange(0,2)
    if com_param == 0:
        com = "Rock"
    elif com_param == 1:
        com = "Paper"
    elif com_param == 2:
        com = "Scissor"
        
    # print " Topic Published : \x1b[1;33m[/perceptionResult]\x1b[1;m"
    # print " \x1b[1;34mHY_Dialog_manager -> KIST_data_collector -> UoS_DMServer\x1b[1;m"
        
    print("User     : \x1b[1;32m{}\x1b[1;m".format(input_user))    
    print("Computer : \x1b[1;33m{}\x1b[1;m".format(com))
    cal = input_param - com_param
    
    result = ""
    if (cal == 1) or (cal == -2):
        result = "\x1b[1;35m{}\x1b[1;m".format("You Win!!^^")
    elif (cal == -1) or (cal == 2) :
        result = "\x1b[1;31m{}\x1b[1;m".format("You Loser ㅠㅠ")
    else:
        result = "\x1b[1;39m{}\x1b[1;m \n".format("Draw~, Try again")
    return result
main()
