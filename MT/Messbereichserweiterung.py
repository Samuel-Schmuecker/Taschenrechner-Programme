# Brogramm zum berechen von innenwiederständen und zur Erweiterung von Messbereichen bei Amper- und Voltmetern

spannungsmessung = int(input("Ampermeter oder Voltmeter (0/1)? "))
Um = float(input("Spannung bei Vollausschlag? "))
Im = float(input("Strom bei vollausschlag? "))

Rm = round(Um/Im,9)

print(Rm, "Ohm")

if spannungsmessung:
    Umess = float(input("Was soll Umess sein? "))

    u = Umess-Um
    Rv = round(u/Im, 9)
    print(f"Rv = {Rv} Ohm")

else : 
    Imess = float(input("Was soll Amess sein? "))

    i = Imess-Im
    Rn = round(Um/i, 9)
    print(f"Shuntwiderstand = {Rn} Ohm")