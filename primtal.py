"""
Uppgift
Skriv ett program som läser ett tal (t.ex. 100) Programmet skall skriva ut alla primtal mellan 1 och det inlästa talet. 
Exempel på utskrift vid körning: Primtal mellan 1 och 100: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

Planering av steg
1. Skapa mainfunktion som i sin tur anropar mindre funktioner.
2. Ta emot input från användaren. 
3. Kolla om input är ett heltal och större än 1. Om inte, be användaren att skriva in ett nytt tal.
4. Om input är > 1, spara i variabel. Tom lista för att samla ihop alla primtal.
5. Loopa igenom alla tal från 1 till inputnummer. I varje iteration, anropa funktion som kollar om talet är ett primtal.
6. Primtalsfunktion tar emot ett tal (börjar på tal 1 och fortsätter med 2, 3, 4 osv upp till inputtalet). Detta blir slutet på rangen i for-loopen.
7. I primtalsfunktion loopar vi igenom alla tal från 2 till talet som skickas in som parameter. Varje iteration kollar om talet är delbart med i. 
   Om talet är delbart med något tal upp till inputtalet så är det ej ett primtal. Returnerar inget tal.
   Om talet Inte är delbart med något av talen från 2 till inputtalet, så är det ett primtal och det returneras.
8. Talen som returneras till primtalsfunktionens anrop sparas i en lista för primtal. 
9. Skriv ut alla tal i listan för primtal.


Felhantering
Om användaren skriver in ett tal som inte är ett heltal så fångas det upp och användaren får skriva in ett nytt tal.
Om användaren skriver in ett tal som är mindre än eller likamed 1 så fångas det upp och användaren får skriva in ett nytt tal.

Brister finns dock i att användaren kan skriva in bokstäver eller specialtecken i inputen innan hen klickar på enter. Detta borde
inte vara möjligt för att förenkla för användaren. Istället för att hantera felaktig input bör man inte tillåta det från början.


"""


def main():

    numberFromInput = getInput()
    primes = []
    for i in range(2, numberFromInput + 1):
        if isPrimeNumber(i):
            primes.append(i)

    if primes:
        print(
            f"Det finns {len(primes)} primtal mellan 1 och {numberFromInput} och dessa är: "
        )
        for prime in primes:
            print(prime, end=" ")


def validateAndConvertInputToInt(string):
    try:
        num = int(string)
        if num <= 1:
            print("Ange ett tal större än 1")
            return None
        return num

    except ValueError:
        print("Felaktig input. Du måste skriva ett heltal. Försök igen. ")
        return None


def getInput():
    givenNumber = None
    while givenNumber is None:
        inputString = input(
            "Skriv ett heltal större än 1 och klicka på enter, ex. 100: "
        )
        givenNumber = validateAndConvertInputToInt(inputString)
    return givenNumber


def isPrimeNumber(number):
    # Loopar från 2 till angivet tal. i startar på 2 eftersom alla tal är delbara med 1 och ökar med 1 för varje iteration.
    for i in range(2, number):
        # Om talet är delbart med i (som är 2, 3, 4, 5, 6 osv upp till angivet tal) så är det inte ett primtal och returnerar inget tal.
        if (number % i) == 0:
            return None
    # Om talet inte är delbart med något av talen från 2 till angivet tal, så är det ett primtal och det returneras.
    else:
        return number


main()
