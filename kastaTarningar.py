"""
Uppgift
Skapa ett program som simulerar kast med två tärningar.


Planering
1. Skapa en mainfunktion som alltid sker i start av programmet.
2. Skapa tärningsfunktion för att generera ett slumpmässigt tal mellan 1 till 6 (tärningskast). Använd random: https://www.geeksforgeeks.org/python-randint-function/
   För dynamisk text för vilken tärning man ska kasta, använd parameter i funktionen och for-loop i mainfunktionen. 
   Kan enkelt lägga till fler tärningar vid senare tillfälle. 
3. Tärningsfunktionen ska returnera talet, som ska sparas vid funktionsanropet till en tärningsvariabel beroende på vilket varv i loopen man är på. 
4. Mainfunktionen ska skriva ut värdet på tärningen.


"""

from random import randint


# Genererar ett slumpmässigt tal mellan 1 till 6 efter att användaren klickat på enter
def getRadnomNumber(diceNumber):
    input(f"Kasta tärning {diceNumber} genom att klicka på enter!")
    dice = randint(1, 6)
    return dice


# Funktion som fortsätter att kasta tärningarna och skriver ut resultaten
def throwDices():

    firstDice = None
    secondDice = None

    for diceNumber in range(2):
        if diceNumber == 0:
            firstDice = getRadnomNumber(diceNumber + 1)
        else:
            secondDice = getRadnomNumber(diceNumber + 1)

    print(f"Tärning 1: {firstDice} \nTärning 2: {secondDice}")


# Mainfunktion som startat programmet. While-loop som frågar om användaren vill avsluta programmet.
def main():
    stopExecution = False

    while stopExecution == False:
        throwDices()
        inputCommand = input("Vill du avsluta? (ja/nej): ")
        if inputCommand == "Ja" or inputCommand == "ja" or inputCommand == "JA":
            stopExecution = True
        elif inputCommand == "Nej" or inputCommand == "nej" or inputCommand == "NEJ":
            stopExecution = False
        else:
            stopExecution = False


main()
