"""
Uppgift
Skapa ett program som simulerar kast med två tärningar.


Planering
1. Skapa en mainfunktion som alltid sker i start av programmet.
2. Användare ska kunna klicka på enter. Detta triggar en funktion som slumpar fram tal mellan 1 till 6 (tärningskast). Använd random: https://www.geeksforgeeks.org/python-randint-function/
3. Någonstans måste de två talen sparas. Enklast i en lista. Detta måste ske i en funktion som hanterar just tärningskast. Värdena ska returneras. 
4. Värdena måste tas emot. Sedan måste mainfunktionen skriva ut tärningarnas värden.
5. Fråga om användaren vill fortsätta kasta. Kastfunktionen anropas inuti en loop.

Brister/Begränsningar
Användaren kan skriva in något annat än ja/nej när man får frågan om att fortsätta och programmet kommer inte att förstå detta.
Borde kanske använda en slags keydown funktion eller event som man kan lyssna på istället för en input, dock är det kanske 
lite överkurs för denna uppgift. 

"""

from random import randint


# Genererar 2 slumpmässiga tal mellan 1 till (till och med) 6 efter att användaren klickat på enter
def throwDices():
    dices = []
    input(f"Kasta tärningarna genom att klicka på enter!")

    for i in range(2):
        dices.append(randint(1, 6))

    return dices


# Mainfunktion som startar programmet. While-loop som frågar om användaren vill avsluta programmet.
def main():
    stopExecution = False

    while stopExecution == False:
        thrownDices = throwDices()
        print(f"Tärningarna visar: {thrownDices[0]} och {thrownDices[1]} prickar")

        inputCommand = input("Vill du avsluta? (ja/nej): ")
        if inputCommand == "Ja" or inputCommand == "ja" or inputCommand == "JA":
            stopExecution = True
        elif inputCommand == "Nej" or inputCommand == "nej" or inputCommand == "NEJ":
            stopExecution = False
        else:
            stopExecution = False


main()
