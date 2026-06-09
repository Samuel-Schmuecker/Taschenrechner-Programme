# Programm dient zur Lagerberechnung bei Wälzlager 

#Beispielwerte:
###

#Aufagbe 33 Kegelrad-Stirnradgetriebe
lagerabstand = -419
xKraefte = [(5400,-202.65,0)]
yKraefte = [(2200,-129.5),(-12200,-289.5)]
zKraefte = [(-16100,-129.5),(-33400,-289.5)]
'''
#Aufgabe 18.27
lagerabstand = 188
xKraefte = [(-22000,105,0)]
yKraefte = [(-25000,109)]
zKraefte = [(-60640,109)]
'''
###
'''
xKraefte = []
yKraefte = []
zKraefte = []
'''
lager1_fx = 0
lager1_fy = 0
lager1_fz = 0

lager2_fy = 0
lager2_fz = 0

'''# Input Daten abfragen
print("Bitte lege deinenen Drehpunkt in Lager eins ")
lagerabstand = float(input("Abstand zwischen den lagern ")) # Da wo die kräfte wirken also a-a 
anzahlXKrafte = int(input("Wie viele X-Kräfte gibt es? "))
anzahlYKrafte = int(input("Wie viele Y-Kräfte gibt es? "))
anzahlZKrafte = int(input("Wie viele Z-Kräfte gibt es? "))


print("x-Kräfte")
for i in range(anzahlXKrafte):
    f = float(input(str(i+1) +". Kraft mit vorzeichen "))
    y = float(input(f"F{i+1} y Abstand "))
    z = float(input(f"F{i+1} z Abstand "))
    xKraefte.append((f,y,z))

print("y-Kräfte")
for i in range(anzahlYKrafte):
    f = float(input(str(i+1) +". Kraft mit vorzeichen "))
    x = float(input(f"F{i+1} x Abstand "))
    yKraefte.append((f,x))

print("z-Kräfte")
for i in range(anzahlYKrafte):
    f = float(input(str(i+1) +". Kraft mit vorzeichen "))
    x = float(input(f"F{i+1} x Abstand "))
    zKraefte.append((f,x))'''


# X- Kräfte Berechenen 
summeXKrafete = 0
for f,y,z in xKraefte:
    summeXKrafete += f
lager1_fx = round(0-summeXKrafete,3)


# y Lager 2 berechnen 
sumM = 0
for f,y,z in xKraefte:
    sumM += -(f*y)
for f,x in yKraefte:
    sumM += f*x

lager2_fy = round(-(sumM/lagerabstand),3)
yKraefte.append((lager2_fy,lagerabstand))

summeYKrafete = 0
for f,x in yKraefte:
    summeYKrafete += f
lager1_fy = round(0-summeYKrafete,3)

# z Kräfte berechnen
sumMy = 0
for f,y,z in xKraefte:
    sumMy += (f*z)
for f,x in zKraefte:
    sumMy += -(f*x)
lager2_fz = round(sumMy/lagerabstand,3)
zKraefte.append((lager2_fz,lagerabstand))

summeZKrafete = 0
for f,x in zKraefte:
    summeZKrafete += f
lager1_fz = round(0-summeZKrafete,3)


print(f"Lager 1: \nfx = {lager1_fx} \nfy = {lager1_fy} \nfz = {lager1_fz}\n")
print(f"Lager 2: \nfy = {lager2_fy} \nfz = {lager2_fz}\n")

#Kräfte verrechnen 
lager1_fr = round(((lager1_fy**2)+(lager1_fz**2))**0.5,3)
lager2_fr = round(((lager2_fy**2)+(lager2_fz**2))**0.5,3)
print(f"Lager 1 FrI = {lager1_fr} \nLager 2 FrII = {lager2_fr}")
