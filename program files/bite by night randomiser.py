import random
import time
import datetime
import os
def load():
       global spring,playerData,mimic,spagetiMan,count
       count = 0
       playerDataFile = open("playerData.txt")
       playerData = playerDataFile.readlines()
       print("Player Data loaded...")
       print(playerData)
       playerDataFile
       spring = (playerData[0])
       spring = spring.lower()
       print(spring)
       mimic = (playerData[1])
       print(mimic)
       spagetiMan = (playerData[2])
       print(spagetiMan)
       playerDataFile.close()
       if spring == "spring unlocked? yes\n":
              spring = True
              count = count + 1
       else:
              spring = False
       if mimic == "mimic unlocked? yes\n":
              mimic = True
              count = count + 1
       else:
              mimic = False
       if spagetiMan == "eneee unlocked? yes\n":
              spagetiMan = True
              count = count + 1
       else:
              spagetiMan = False
       if count == 0:
              print("ERROR NO CHARACTERS SELECTED")
              os.remove("playerData.txt")
              print("player data deleted restarting")
              time.sleep(1)
              quit()

       time.sleep(1)
print ('''
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪 Welcome to Bite by night randomiser V3 🟪
       🟪🟪🟪🟪🟪🟪🟪 this is a wip  🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       ''')
update = datetime.datetime(2026 , 5 , 30)
hint = datetime.datetime(2026 , 5 , 10)
currentDate = datetime.datetime.now()
if os.path.exists("playerData.txt"):
       load()
else:
       print("player data not found")
       with open("playerData.txt", "x") as playerDataFile:
             ()
       playerDataFile = open("playerData.txt" , "w")
       print("Hi i cant find your player data this means we have to create one please answer these quick questions")
       tempSpring = str(input("Do you have Springtrap| please say 'yes' or 'no'"))
       tempmimic = str(input("do you have the mimic|please say 'yes' or 'no'"))
       tempenared = str(input("do you have enared | please say 'yes' or 'no' "))
       tempSpring = tempSpring.lower()
       tempmimic = tempmimic.lower()
       tempenared = tempenared.lower()
       playerDataFile.writelines("spring unlocked? " + tempSpring + "\n")
       playerDataFile.writelines("mimic unlocked? " + tempmimic + "\n")
       playerDataFile.writelines("eneee unlocked? " + tempenared + "\n")
       playerDataFile.close()
       load()
if currentDate > update:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       end = input("click enter to exit")
       quit()
elif currentDate > hint:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       print ("resuming program")
       time.sleep(1)
temp = input ("do you want to reset your player DATA? (yes or no)")
temp = temp.lower()
if temp == "yes":
       if os.path.exists("playerData.txt"):
              os.remove("playerData.txt")
              print("file deleted exiting")
              time.sleep(1)
              quit()
       else:
              print("ERROR NO FILE EXSITS")
              quit()
while True:
       char = input("select enter to choose a killer") #("do you need killer 'k', surviver's' or both 'b' ")
       #char = char.lower()
       correct = False
       if 2+2 == 4:#char == "k" or char == "b":
              while correct == False:
                     num = random.randint(1,3) #random.randint(1,4)
                     if num == 1 and spring == True:
                            print ("springtrap")
                            correct = True
                     elif num == 2 and mimic == True:
                            print ("the mimic")
                            correct = True
                     elif num == 3 and spagetiMan == True:
                            print ("enared")
                            correct = True
                     # elif num == 4:
                     #        print ("puppet")
                     else:
                            print("Loading ...")
                            time.sleep(0.1)
       else:
              print("Error please enter valid data")