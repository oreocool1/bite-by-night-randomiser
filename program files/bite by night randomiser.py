import random
import time
import datetime
import os
print ('''
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪 Welcome to Bite by night randomiser V2 🟪
       🟪🟪🟪🟪🟪🟪🟪 this is a wip  🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       ''')
update = datetime.datetime(2026 , 5 , 30)
hint = datetime.datetime(2026 , 5 , 10)
currentDate = datetime.datetime.now()
# if os.path.exists("playerData.txt"):
#        with open("playerData.txt" , "r") as playerDataFile:
#               playerData = playerDataFile.readlines()
#        print("Player Data loaded...")
#        time.sleep(1)
# else:
#        print("player data not found")
#        with open("playerData.txt", "x") as playerDataFile:
#              ()
#        playerDataFile = open("playerData.txt" , "w")
#        print("Hi i cant find your player data this means we have to create one please answer these quick questions")
#        tempSpring = str(input("Do you have Springtrap| please say 'yes' or 'no'"))
#        tempmimic = str(input("do you have the mimic|please say 'yes' or 'no'"))
#        tempenared = str(input("do you have enared | please say 'yes' or 'no' "))
#        tempSpring = tempSpring.lower()
#        tempmimic = tempmimic.lower()
#        tempenared = tempenared.lower()
#        playerDataFile.writelines("spring:  " + tempSpring + os.linesep)
#        playerDataFile.writelines("mimic:  " + tempmimic + os.linesep)
#        playerDataFile.writelines("eneee:  " + tempenared + os.linesep)
#        playerDataFile.close()
if currentDate > update:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       end = input("click enter to exit")
       quit()
elif currentDate > hint:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       print ("resuming program")
       time.sleep(1)
while True:
       char = input("do you need killer 'k', surviver's' or both 'b' ")
       char = char.lower()
       correct = False
       
              
       if char == "k" or char == "b":
              while correct == False:
                     num = random.randint(1,3)
                     if num == 1:
                            print ("springtrap")
                            correct = True
                     elif num == 2:
                            print ("the mimic")
                            correct == True
                     elif num == 3:
                            print ("enared")
                            correct ==True
                     else:
                            print("Error found retrying ...")
                            time.sleep(0.1)
       else:
              print("Error please enter K (killer) as S (surviver is unter development) ")