#Programm zu bestimmung der Gaußschen verteilung Quantile z

xMittel = float(input("Mittelwert = "))
u = float(input("Varianz u = "))
xOberGrenze = float(input("x Obergrenze = "))

z = round((xOberGrenze-xMittel)/u,6)
print()
print("Quantile z")
print("z = ",z)

print()
print("Tabelle: Quantile der Normalverteilung")
a = float(input("a-Wert zu z-Wert = "))

w = round(a*100,3)

print("Wahrscheinlichkeit für \nx < ",xOberGrenze)
print(w,"%")

print()
untergrenze = int(input("Untergrezne? (0/1) "))

if untergrenze:
    xUnterGrenze = float(input("x Untergrenze = "))

    zu = round((xUnterGrenze-xMittel)/u,6)

    if zu < 0:
        zuMinus = True
        zu = abs(zu)
    else:
        zuMinus = False

    print()
    print("zUntergrenze = ", zu)
    au = float(input("a-Wert zu z-Wert ="))

    wu = round(au*100,3)

    if zuMinus:
        wu = 100-wu
    
    print()
    print("Wahrscheinlichkeit für \nx > ",xUnterGrenze)
    print(wu,"%")

    wges = w-wu
    print()
    print("Wahrscheinlichkeit für \nx zwichen xu und xo")
    print(wges,"%")
