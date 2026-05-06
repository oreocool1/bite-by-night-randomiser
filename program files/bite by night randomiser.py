import random
import time
import datetime
import os
def loadKiller():
       global The_Rotten,playerData,The_Project,Dopplelganger,count
       count = 0
       with open ("killerData.txt") as playerDataFile:
              playerData = playerDataFile.read()
              print ("--killer Data Loaded--")
              print(playerData)
              time.sleep(1.5)
       playerDataFile = open("KillerData.txt")
       playerData = playerDataFile.readlines()
       if len(playerData) < 3:
              print("There is an error with your file")
              playerDataFile.close()
              os.remove("killerData.txt")
              quit()
       The_Rotten = (playerData[0])
       The_Project = (playerData[1])
       Dopplelganger = (playerData[2])
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
       # print(The_Rotten) #dev tool
       # print(The_Project) # dev tool
       # print (Dopplelganger) # dev tool
       # print(count) # dev tool
       if count == 0:
              print("ERROR NO CHARACTERS SELECTED")
              os.remove("KillerData.txt")
              print("player data deleted restarting")
              time.sleep(1)
              quit()

def loadskin():
       global Toon,Spartan,PitRabbit,Hoax,decition
       with open ("skinData.txt") as playerSkinFile:
              print("--Skin Data loaded--")
              playerSkinprint = playerSkinFile.read()
              print(playerSkinprint)
       playerSkinFile = open ("skinData.txt")
       playerSkinData = playerSkinFile.readlines()
       #print(len(playerSkinData)) # dev tool
       if len(playerSkinData) < 5:
              print("error")
              quit()
       decition = (playerSkinData[0])
       #print(decition)#dev tool
       if decition == "skin load?yes\n":
              Toon = (playerSkinData[1])
              Spartan = (playerSkinData[2])
              PitRabbit = (playerSkinData[3])
              Hoax = (playerSkinData[4])
              count = 0
              if Toon == "Toon unlocked?yes\n":
                     Toon = True
                     count = count+1
              else:
                     Toon = False
              if Spartan == "Spartan unlocked?yes\n":
                     Spartan = True
                     count = count+1
              else:
                     Spartan = False
              if PitRabbit =="PitRabbit unlocked?yes\n":
                     PitRabbit = True
                     count = count+1
              else:
                     PitRabbit = False
              if Hoax == "Hoax unlocked?yes\n":
                     Hoax = True
                     count = count+1
              else:
                     Hoax = False
              
              # print (Toon) #dev tool
              # print(Spartan) # dev tool
              # print(PitRabbit) # dev tool
              # print(Hoax) # dev tool
              # print(count) # dev tool
              if count == 0:
                     print("error")
                     playerSkinFile.close()
                     os.remove("skinData.txt")
       else:
              print("skin randomiser off")
       time.sleep(1)
print ('''
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪 Welcome to Bite by night randomiser V4 🟪
       🟪🟪🟪🟪🟪🟪🟪 this is a wip  🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       ''')
for x in range(4):
       print("loading...")
       time.sleep(1)
print("Loaded!\ncreated by oreocool1")
time.sleep(1.5)
update = datetime.datetime(2026 , 5 , 30)
hint = datetime.datetime(2026 , 5 , 8)
currentDate = datetime.datetime.now()
if os.path.exists("KillerData.txt"):
       loadKiller()
else:
       print("player data not found")
       with open("KillerData.txt", "x") as playerDataFile:
             ()
       playerDataFile = open("KillerData.txt" , "w")
       print("Hi i cant find your player data this means we have to create one please answer these quick questions")
       tempThe_Rotten = "yes"#str(input("Do you have The Rotten| please say 'yes' or 'no'"))
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
if os.path.exists("skinData.txt"):
       loadskin()
else:
       with open ("skinData.txt", "x") as skinDataFile:
              ()
       skinDataFile = open ("skinData.txt","w")
       temp = input("Do you want to add your skins to the randomiser?")
       temp = temp.lower()
       skinDataFile.writelines("skin load?" + temp + "\n")
       #print (temp) #dev tool
       if temp == "yes":
              print("okay it seems we dont have your skins on file answer these questions to make a new one")
              with open ("skinData.txt","a") as skinDataFile:
                     Toon = input("Do you have the Toon skin?")
                     Spartan = input("Do you have the Spartan skin?")
                     PitRabbit = input("Do you have Pit Rabbit?")
                     Hoax = input("Do you have the Hoax skin?")
                     Toon = Toon.lower()
                     Spartan = Spartan.lower()
                     PitRabbit = PitRabbit.lower()
                     Hoax = Hoax.lower()
                     skinDataFile.writelines("Toon unlocked?" + Toon + "\n")
                     skinDataFile.writelines("Spartan unlocked?" + Spartan + "\n")
                     skinDataFile.writelines("PitRabbit unlocked?" + PitRabbit + "\n")
                     skinDataFile.writelines("Hoax unlocked?" + Hoax + "\n")
              loadskin()
       else:
              with open ("skinData.txt","a") as skinDataFile:
                     print("No has been selected")
                     for x in range (4):
                            skinDataFile.write("empty\n")

if currentDate > update:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       end = input("click enter to exit")
       quit()
elif currentDate > hint:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       print ("resuming program")
       time.sleep(1)
temp = input ("do you want to reset your player DATA? (none(n), killer_data (k), Skin_data(s), all(a))")
temp = temp.lower()
if temp == "k":
       if os.path.exists("KillerData.txt"):
              os.remove("KillerData.txt")
              print("killer data file deleted exiting")
              time.sleep(1)
              quit()
       else:
              print("ERROR NO FILE EXSITS")
              quit()
elif temp == "s":
       if os.path.exists("skinData.txt"):
              os.remove("skinData.txt")
              print("skin data file deleted exiting")
              time.sleep(1)
              quit()
       else:
              print("ERROR NO FILE EXSITS")
              quit()
elif temp == "a":
       if os.path.exists("killerData.txt"):
              os.remove("killerData.txt")
              print("killer data removed...")
              if os.path.exists("skinData.txt"):
                     os.remove("skinData.txt")
                     print("All data removed")
                     quit()
              else:
                     print("All data removed (skin data not located)")
                     quit()
       elif os.path.exists("skinData.txt"):
              os.remove("skinData.txt")
              print("All data removed(killer data not found)")
              quit()
       else:
              print("error no file exsists")
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
                            time.sleep(0.1)
                            if decition == "skin load?yes\n":
                                   temp1 = False
                                   while temp1 == False:
                                          temp = random.randint(0,3)
                                          if temp == 0 and Toon == True:
                                                 print ("Skin: Toon")
                                                 temp1 = True
                                          elif temp == 1 and Spartan == True:
                                                 temp1 = True
                                                 print("Skin:  Spartan")
                                          elif temp == 2 and PitRabbit == True:
                                                 print("Skin:  Pit rabbit")
                                                 temp1 = True
                                          elif temp == 3 and Hoax == True:
                                                 print("Skin:  Hoax")
                                                 temp1 = True
                                          else:
                                                 print("loading...")
                                                 time.sleep(0.1)
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