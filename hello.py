

for i in range(1, 101):
    if i % 3 and i % 5 == 0:
        print("fizz,bezz",end=" ")
    elif i % 3 == 0:
        print("fizz",end=" ")
    elif i % 5 == 0:
        print("bezz",end=" ")
    else:
        print(i,end=" ")


lista = list(range(10))

for i in lista:
    print(f"")
print(lista)

# Detta program beräknar summan av ett antal tal

i = 0
while i < 3: # Start yttre loop
    j = 0
    while j < 3: # Start inre loop
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
print("Programmet avslutas")


summa = 0
while True:
    tal = int(input("Ange ett valfritt tal, noll avslutar -> "))
    if tal == 0:
        break
    if tal < 0:
        continue
    summa += tal
print(f"Summan av de inmatade positiva talen är {summa}")





"""
import random
Gissaträtt = False

x = random.randint (1,100)
while not Gissaträtt:

    första = int(input("skriv en siffra"))

    if första == x:
        print("Rätt")
        Gissaträtt = True
    elif första < x:
        print("högre")
    else:
        print("lägre")

"""

