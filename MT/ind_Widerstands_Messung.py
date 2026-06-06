# Programm zur bestimmung von Widerständen durch eine Indirekte Messung

# Angaben Einlesen
print("Werte ohne Einheiten eingeben")
print("Bei Unbekannte Werte 0 eingben")

stromRichtg = int(input("Stromrichtig? (0/1) "))
if stromRichtg:
    Um = float(input("U = "))
    Im = float(input("I = "))
    RiA = float(input("RiA = "))

    stromRichtg = {"Um":Um,"Im":Im,"RiA":RiA}

spannungsRichtg = int(input("Spannungsrichtig? (0/1) "))
if spannungsRichtg:
    Um = float(input("U = "))
    Im = float(input("I = "))
    RiV = float(input("RiV = "))
    
    spannungsRichtg = {"Um":Um,"Im":Im,"RiV":RiV}

if stromRichtg:
    Rm = round(stromRichtg["Um"]/stromRichtg["Im"],6)
    stromRichtg["Rm"] = Rm
    R = Rm-stromRichtg["RiA"]
    stromRichtg["R"] = R
    stromRichtg["F"] = stromRichtg["RiA"]
    stromRichtg["f"] = round((stromRichtg["RiA"]/R)*100,2)

if spannungsRichtg:
    Rm =  round(spannungsRichtg["Um"]/spannungsRichtg["Im"],6)
    spannungsRichtg["Rm"] = Rm
    R = round(1/(1/Rm - 1/spannungsRichtg["RiV"]),6)
    spannungsRichtg["R"] = R
    spannungsRichtg["F"] = Rm -R
    spannungsRichtg["f"] = round((spannungsRichtg["F"]/R)*100,2)


if stromRichtg:
    print("StromRichtig")
    for key in stromRichtg:
        print(f"{key} = {stromRichtg[key]}") 

if spannungsRichtg:
    print("SpannungsRichtig")
    for key in spannungsRichtg:
        print(f"{key} = {spannungsRichtg[key]}") 