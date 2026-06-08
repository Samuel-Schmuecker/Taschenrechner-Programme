# Programm dient zur Lagerberechnung bei Wälzlager 

xKraefte = []
yKraefte = []

lager1_fx = 0
lager1_fy = 0

lager2_fy = 0

# Input Daten abfragen
print("Bitte lege deinenen Drehpunkt in Lager eins ")
lagerabstand = float(input("Abstand zwischen den lagern ")) # Da wo die kräfte wirken also a-a 
anzahlXKrafte = int(input("Wie viele X-Kräfte gibt es? "))
anzahlYKrafte = int(input("Wie viele Y-Kräfte gibt es? "))

print("x-Kräfte")
for i in range(anzahlXKrafte):
    f = float(input(str(i+1) +". Kraft mit vorzeichen "))
    x = float(input(f"F{i+1} x Abstand "))
    y = float(input(f"F{i+1} y Abstand "))
    xKraefte.append((f,x,y))

print("y-Kräfte")
for i in range(anzahlYKrafte):
    f = float(input(str(i+1) +". Kraft mit vorzeichen "))
    x = float(input(f"F{i+1} x Abstand "))
    y = float(input(f"F{i+1} y Abstand "))
    yKraefte.append((f,x,y))


# X- Kräfte Berechenen 
summeXKrafete = 0
for f,x,y in xKraefte:
    summeXKrafete += f
lager1_fx = 0-summeXKrafete


# F Lager 2 berechnen 
sumM = 0
for f,x,y in xKraefte:
    sumM += -(f*y)
for f,x,y in yKraefte:
    sumM += f*x

lager2_fy = -(sumM/lagerabstand)
yKraefte.append((lager2_fy,lagerabstand,0))

summeYKrafete = 0
for f,x,y in yKraefte:
    summeYKrafete += f
lager1_fy = 0-summeYKrafete

print(f"Lager 1: fx = {lager1_fx}; fy = {lager1_fy}")
print(f"Lager 2: fy = {lager2_fy}")
