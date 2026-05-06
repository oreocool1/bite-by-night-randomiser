import random
import time
import datetime
import os
def loadKiller():
       global The_Rotten,playerData,The_Project,Dopplelganger,count
       count = 0
       playerDataFile = open("KillerData.txt")
       playerData = playerDataFile.readlines()
       if len(playerData) < 3:
              print("There is an error with your file")
              playerDataFile.close()
              os.remove("killerData.txt")
              quit()
       print("Player Data loaded...")
       print(playerData)
       
       The_Rotten = (playerData[0])
       print(The_Rotten)
       The_Project = (playerData[1])
       print(The_Project)
       Dopplelganger = (playerData[2])
       print(Dopplelganger)
       playerDataFile.close()
       if The_Rotten == "The Rotten unlocked? yes\n":
              The_Rotten = True
              count = count + 1
       else:
              The_Rotten = False
       if The_Project == "The Project unlocked? yes\n":
              The_Project = True
              count = count + 1
       else:
              The_Project = False
       if Dopplelganger == "Dopplelganger unlocked? yes\n":
              Dopplelganger = True
              count = count + 1
       else:
              Dopplelganger = False
       # print(The_Rotten)
       # print(The_Project)
       # print (Dopplelganger)
       # print(count)
       if count == 0:
              print("ERROR NO CHARACTERS SELECTED")
              os.remove("KillerData.txt")
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
print("loading...")
time.sleep(2.5)
update = datetime.datetime(2026 , 5 , 30)
hint = datetime.datetime(2026 , 5 , 10)
currentDate = datetime.datetime.now()
if os.path.exists("KillerData.txt"):
       loadKiller()
else:
       print("player data not found")
       with open("KillerData.txt", "x") as playerDataFile:
             ()
       playerDataFile = open("KillerData.txt" , "w")
       print("Hi i cant find your player data this means we have to create one please answer these quick questions")
       tempThe_Rotten = str(input("Do you have The Rotten| please say 'yes' or 'no'"))
       tempThe_Project = str(input("do you have The Project|please say 'yes' or 'no'"))
       tempDopplelganger = str(input("do you have Dopplelganger | please say 'yes' or 'no' "))
       tempThe_Rotten = tempThe_Rotten.lower()
       tempThe_Project = tempThe_Project.lower()
       tempDopplelganger = tempDopplelganger.lower()
       playerDataFile.writelines("The Rotten unlocked? " + tempThe_Rotten + "\n")
       playerDataFile.writelines("The Project unlocked? " + tempThe_Project + "\n")
       playerDataFile.writelines("Dopplelganger unlocked? " + tempDopplelganger + "\n")
       playerDataFile.close()
       print("file closed")
       loadKiller()
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
       if os.path.exists("KillerData.txt"):
              os.remove("KillerData.txt")
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
                     if num == 1 and The_Rotten == True:
                            print ("The Rotten")
                            correct = True
                     elif num == 2 and The_Project == True:
                            print ("The Project")
                            correct = True
                     elif num == 3 and Dopplelganger == True:
                            print ("Dopplelganger")
                            correct = True
                     # elif num == 4:
                     #        print ("puppet")
                     else:
                            print("Loading ...")
                            time.sleep(0.1)
       else:
              print("Error please enter valid data")