#Main.py

#Credit, Keep this in
print("All Credit to SkyeGamesYT")


def exit1():
    input("Press enter to Exit")


def menu():
  print("-"*50)
  x = input("Choice 1\nChoice 2\nChoice 3")
  print("-"*50)
  if x == "1":
    print("Choice 1")
    #Code for choice 1
  if x == "2":
    print("Choice 2")
      #Code for choice 2
  if x == "3":
    print("Choice 3")
        #Code for choice 3
        
def Playagain():
          y = input("Print again? Y/N: ")
          if y == "Y":
            menu()
            if y == "N":
              exit()



#Actual Menu code
menu()
Playagain()