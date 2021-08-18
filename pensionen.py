program_run = True
print("--------------------------------------")
print("Välkommen till denna pensionsimulator")
print("--------------------------------------")

while program_run:  #While loopen iterarar koden så länge program_run är lika med True. 
    try:   #Använder try här för att testa om det genereras fel, mest med tanke på åldersfrågan då programmet kraschar om man missar att svara på frågan
        name = input("Vad heter du i förnamn?\n")
        age = int(input("Hur gammal är du?\n"))   #Eftersom input blir datatyp string så gör jag en typomvandling till integer med hjälp av int()

    except ValueError:   #Felmeddelande om användaren inte skrivit in sin ålder
        print("Oops nått blev fel med din ålder, försök igen..")
        continue
    if len(name) <= 0:   #Felmeddelande om användaren inte skrivit in sitt namn
        print("Nått blev fel, skriv ditt namn igen..")
        continue
    elif age < 0:   #Felmeddelande om användaren skriver in ett negativt tal
        print("Din ålder kan inte vara negativ..")
    else:   #Här körs resten av programmet då inga fel hittats.
        years_to_pension = 65 - age
        print(f"Hej {name}. Du går i pension om {years_to_pension} år.")
        program_run = False    #Här avslutas programmet då program_run ändras till False 

