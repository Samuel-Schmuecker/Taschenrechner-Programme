#Berechung der Lebensdauer von Wälzlagern

#Testwerte aufgeb 14.18
#lager1 = {"Fa": 2000, "Fr": 8500, "e": 0.35, "C": 92000, "X": 0.4, "Y": 1.74, "n": 1500, "Kugeln?" : 0}
#lager2 = {"Fr": 6200, "e": 0.31, "C": 60000, "X": 1, "Y": 1.9, "n": 1500, "Kugeln?" : 0}
#Testwerte Aufgabe 33
#lager1 = {"Fa": 5400, "Fr": 21450, "e": 0.35, "C": 420000, "X": 0.4, "Y": 1.74, "n": 1000, "Kugeln?" : 0}
#lager2 = {"Fr": 29905, "e": 0.35, "C": 420000, "X": 1, "Y": 1.74, "n": 1000, "Kugeln?" : 0}
#Testwerte Aufgabe 18.27
#lager1={'Fa': 22000.0, 'Fr': 34200.0, 'e': 0.44, 'C': 490000.0, 'X': 0.4, 'Y': 1.38, 'n': 1500.0, 'Kugeln?': 0}
#lager2={'Fr': 35230.0, 'e': 0.44, 'C': 490000.0, 'X': 0.4, 'Y': 1.38, 'n': 1500.0, 'Kugeln?': 0}

# Eingabe der Werte aus dem Tabellen Buch


print("Lager1:")
lager1 = {
    "Fa":float(input("Fa: ")), 
    "Fr" : float(input("Fr: ")),
    "e" : float(input("e: ")),
    "C" : float(input("C: ")),
    "X" : float(input("X: ")),
    "Y" : float(input("Y: ")),
    "n" : float(input("n: ")),
    "Kugeln?" : bool(int(input("Kugellager? 0 oder 1: ")))
    }


print("Lager2:")
lager2 = { 
    "Fr" : float(input("Fr: ")),
    "e" : float(input("e: ")),
    "C" : float(input("C: ")),
    "X" : float(input("X: ")),
    "Y" : float(input("Y: ")),
    "n" : float(input("n: ")),
    "Kugeln?" : bool(int(input("Kugellager? 0 oder 1: ")))
    }




# Bestimmung des Kräfteverhältnisses 
# v = Verhälzniss Fr zu Y des Lagers 
# w = Wert mit dem fa verglichen wird
fall = 0
v1 = lager1["Fr"]/lager1["Y"]
v2 = lager2["Fr"]/lager2["Y"]
w = 0.5*(v1-v2)

if v1 <= v2 : 
    fall = 1
elif (lager1["Fa"]>w):
    fall = 2 
else:
    fall = 3

# Berechnung der Axialkräfte:
match fall:
    case 1|2:
        lager1["Fa1"] = lager1["Fa"]+0.5*v2
        lager2["Fa2"] = 0.5*v2
    case 3: 
        lager1["Fa1"] = 0.5*v1
        lager2["Fa2"] = 0.5*v1-lager1["Fa"]       


# Berechnung der Lagerbelastung P:
if (lager1["Fa1"]/lager1["Fr"])>lager1["e"]:
    lager1["P"] = lager1["X"]*lager1["Fr"] + lager1["Y"]*lager1["Fa1"]
else: 
    lager1["P"] = 1*lager1["Fr"]

if (lager2["Fa2"]/lager2["Fr"])>lager2["e"]:
    lager2["P"] = lager2["X"]*lager2["Fr"] + lager2["Y"]*lager2["Fa2"]
else: 
    lager2["P"] = 1*lager2["Fr"] 


# Berechnung der Lebensdauer 
def lebensdauer(lager:dict)->dict:
    if lager["Kugeln?"]:
        p = 3
    else:
        p = 10/3

    lager["L10"] = (lager["C"]/lager["P"])**p

    if lager["n"] != 0:
        lager["L10h"] = (lager["L10"]*10**6)/(60*lager["n"])

    return(lager)

# Für Lager 1 und 2
lager1 = lebensdauer(lager1)
lager2 = lebensdauer(lager2)

# Ausgabe der Werte
print("Lager 1:")
print("Fa1 = ", lager1["Fa1"])
print("L10 = ", lager1["L10"])
if lager1["n"]:
    print("L10h = " , lager1["L10h"])

print()

print("Lager 2:")
print("Fa2 = ", lager2["Fa2"])
print("L10 = ", lager2["L10"])
if lager2["n"]:
    print("L10h = ", lager2["L10h"])