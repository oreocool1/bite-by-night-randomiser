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
if os.path.exists("playerData.txt"):
       playerDataFile = open("playerData.txt" , "r")
       playerData = playerDataFile.readlines()
       print("Player Data loaded...")
       time.sleep(1)
else:
       print("player data not found")
       playerDataFile = open("playerData.txt", "x")
if currentDate > update:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       end = input("click enter to exit")
       quit()
elif currentDate > hint:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       print ("resuming program")
       time.sleep(1)
while 2+2 == 4:
       char = input("do you need killer 'k', surviver's' or both 'b' ")
       char = char.lower()
       correct = False
       
              
       if char == "k" or char == "b":
              while correct == False:
                     num = random.randint(1,3)
                     if num == 1:
                            print ("springtrap")
                            #temp = 1 #random.randint(1,2)
                            #if temp == 1:
                            #print ("skin:into the pit")
                            #else:
                            #     print("error")
                            correct = True
                     elif num == 2:
                            print ("the mimic")
                            correct == True
                     elif num == 3:
                                   print ("enared")
                                   correct ==True
                                   #temp = random.randint(1,2)
                     else:
                            print("Error found retrying ...")
                            time.sleep(0.1)
       else:
              print("Error please enter K (killer) as S (surviver is unter development) ")