import random
import time
import datetime
print ('''
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪 Welcome to Bite by night randomiser V1 🟪
       🟪🟪🟪🟪🟪🟪🟪 this is a wip  🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
       ''')
update = datetime.datetime(2026 , 5 , 5)
currentDate = datetime.datetime.now()
if currentDate > update:
       print ("please update version https://github.com/oreocool1/bite-by-night-randomiser")
       end = input("click enter to exit")
       quit()
while 2+2 == 4:
       place=input("what map are you on 'f' 'm' 'p' ")
       char = input("do you need killer 'k', surviver's' or both 'b' ")
       place = place.lower()
       char = char.lower()
       correct = False
       
              
       if char == "k" or char == "b":
              while correct == False:
                     num = random.randint(1,3)
                     if num == 1:
                            if place == "m" or place == "p":
                                   print ("springtrap")
                                   #temp = 1 #random.randint(1,2)
                                   #if temp == 1:
                                   #       print ("skin:into the pit")
                                   #else:
                                   #     print("error")
                                   correct = True
                     elif num == 2:
                            print ("the mimic")
                            correct == True
                     elif num == 3:
                            if place == "f" or place == "m":
                                   print ("enared")
                                   correct ==True
                                   #temp = random.randint(1,2)
                     else:
                            print("Error found retrying ...")
                            time.sleep(0.1)