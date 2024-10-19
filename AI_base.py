from time import sleep
from random import randint
Dove = 50
Hawk = 50
count = 0 
total = Hawk + Dove
Hpercent = Hawk / total * 100
Dpercent = Dove / total * 100
while Hawk > 0 and Dove > 0:
    total = Hawk + Dove
    count += 1
    print ("Day " + str(count) )
    Hpercent = Hawk / total * 100
    Dpercent = Dove / total * 100
    print ("Hawk percent: " + str(Hpercent) + "%     Dove percent:" + str(Dpercent) + "%")
    print ("Hawk amount:" + str(Hawk) + "     Dove amount:" + str(Dove))
    sleep (5)
    for i in range(25):
        meeting = randint(1,4)
        if meeting == 4 :
            if randint (1,2) == 2:
                Hawk = Hawk + 1
            if randint (1,2) == 2 : 
                Dove = Dove - 1
        if  meeting == 3:
            for i in range(2):
                if (randint(1,2) == 2):
                    Hawk = Hawk - 1
        if meeting == 2:
            for i in range (2):
                if (randint(1,2)):
                    Dove = Dove + 1
        if meeting == 1 :
            solo = randint(1,2)
            if solo == 1:
                Hawk = Hawk + 1
            if solo == 2 :
                Dove = Dove + 1
total = Hawk + Dove
count += 1
print ("Day " + str(count) )
Hpercent = Hawk / total * 100
Dpercent = Dove / total * 100
print ("Hawk percent: " + str(Hpercent) + "%     Dove percent:" + str(Dpercent) + "%")
print ("Hawk amount:" + str(Hawk) + "     Dove amount:" + str(Dove))
  
