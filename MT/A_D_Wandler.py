
################################
#Testwerte
n=8
mb=5
x=1.37

fomatString = "{:0.3e}"

#n = int(input("Anzahl Bits? "))
#mb = float(input("Messbereich? (+/-) "))

#Quantisierungsstufe
q = round(mb/(2**n - 1),6)
print("Q = U_LSB =", fomatString.format(q))

fmax = 0.5*q
print("Fmax = ",fomatString.format(fmax))

print()
#x = float(input("Gesuchter Messwert? "))

anzeige = round(x/q,6)
ausgabeWert = round(anzeige)
rest = ausgabeWert-anzeige
binWert = bin(ausgabeWert)
f = round(rest*q,6)

print(x,"/",q," = ",anzeige)
print("A/D Ausagbe = ",ausgabeWert)
print("Bin = ", binWert)
print("Fehler = ",fomatString.format(f))
