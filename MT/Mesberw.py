# Brogramm zum berechen von innenwiederständen und zur Erweiterung von Messbereichen bei Amper- und Voltmetern

spannungsmessung = int(input("Ampermeter oder \nVoltmeter (0/1)? "))
Um = float(input("U bei Vollausschlag? "))
Im = float(input("I bei vollausschlag? "))

Rm = round(Um/Im,9)

print("Ri = ",Rm, "Ohm")

if spannungsmessung:
    Umess = float(input("Was soll Umess sein? "))

    u = Umess-Um
    Rv = round(u/Im, 9)
    print("Rv = ",Rv,"Ohm")

else : 
    Imess = float(input("Was soll Amess sein? "))

    i = Imess-Im
    Rn = round(Um/i, 9)
    print("Shuntwiderstand = ",Rn,"Ohm")