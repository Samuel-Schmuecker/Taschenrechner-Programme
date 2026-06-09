#Pogramm zu Berechnung des Haußen Fehlers 
#Alle eingaben ohne Einheiten

##########################################
#Testwerte:                              #
#anzahl = 5                              #
#messwerte = [1, 1.1 ,0.95 ,1.15 ,1.2]   #
###########################################

fomatString = "{:0.3e}"

#1. Mittelwert Bilden
anzahl = int(input("Anzahl Messwert? "))
messwerte = []
for i in range(anzahl):
    text = "X"+str(i+1)+" = "
    eingabe = float(input(text))
    messwerte.append(eingabe)


xMittel = 0
for x in messwerte:
    xMittel += x
xMittel = round(xMittel/anzahl,6)

print()
print("Mittelwert = ",fomatString.format(xMittel))

#2. Standardabweichung s
nenner = 0
for x in messwerte:
    nenner += (x-xMittel)**2
s = round((nenner/(anzahl-1))**0.5,6)

print("Standardabweichung\ns = ",s)

#3. Bildung er empirishen Standardabweichung u
u = round(s/(anzahl**0.5),6)
print()
print("empirische Standartabweichung")
print("u = ",fomatString.format(u))

#4. Ergebniss 
print()
print("Gewünschte Sicherheit:")
print("68,3%; 95,5%; 99,7%; 99,9%")
print("Input 0,1,2,3,4 (0=Abbruch)")
sicherheit = int(input(""))

if sicherheit:   
    print()
    print("xMittel +/- ",sicherheit,"*u ")
    deltaX = sicherheit*u
    print(xMittel," +/- ", fomatString.format(deltaX))
    print()

#Berüksichtigung des Student-t-Faktors
n = [3,5,10,100]
s68 = [1.32, 1.15, 1.06, 1] #Faktoren für 68,3% Sicherheit 
s95 = [4.3, 2.8, 2.3, 2]
s99 = [19.2, 6.6, 4.1, 3.1]


if anzahl in n:
    i = n.index(anzahl)

    if sicherheit == 1:
        print("Verbessert: (Student-t)")
        deltaX =  round(s68[i]*u,6)
        print(xMittel,"+/-", fomatString.format(deltaX) )

    elif sicherheit == 2:
        print("Verbessert: (Student-t)")
        deltaX = round(s95[i]*u,6)
        print(xMittel,"+/-", fomatString.format(deltaX) )
    
    elif sicherheit == 3:
        print("Verbessert: (Student-t)")
        deltaX = round(s99[i]*u ,6)
        print(xMittel,"+/-", fomatString.format(deltaX))

    else:
        print("keine gespeicheten Wete für Student-t")
else:
    print("Anzahl nicht in Student-t")

#5. Berechnung des relativen Fehlers
f = round((deltaX/xMittel)*100,3)
print()
print("relativer Fehler f")
print("f = ",f,"%")
 
 