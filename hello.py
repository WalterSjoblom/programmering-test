
Gissaträtt = False
import random 
while not Gissaträtt:


    x = random.randint (1,100)

    första = int(input("skriv en siffra"))

    if första == x:
        print("Rätt")
        Gissaträtt = True
    if första < x:
        print("högre")
    else:
        print("lägre")



lista = [10,20,30,40]






