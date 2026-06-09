import matplotlib.pyplot as plt 
#Testwerte:

lagerabstand = 160
xKrafte = [(300,0,85.55)]
yKrafte = [(-1120,60)]
zKrafte = [(-420,60)]

lagerA = {"Fx":None,"Fy":None,"Fz":None}
lagerB = {"Fx":None,"Fy":None,"Fz":None}

'''
print("Drehpunkt in Lager A legen!")
lagerabstand = float(input("Abstand zwischen den Lagern: "))

anzahlX = int(input("Wie viele X-Kräfte gibt es? "))
xKrafte = []
for i in range(anzahlX):
    f = float(input(f"F{i+1} = "))
    y = float(input("y-Abstand = "))
    z = float(input("z-Abstand = "))
    xKrafte.append((f,y,z))

anzahlY = int(input("Wie viele Y-Kräfte gibt es? "))
yKrafte = []
for i in range(anzahlY):
    f = float(input(f"F{i+1} = "))
    x = float(input("x-Abstand = "))
    yKrafte.append((f,x))

anzahlZ = int(input("Wie viele Z-Kräfte gibt es? "))
zKrafte = []
for i in range(anzahlZ):
    f = float(input(f"F{i+1} = "))
    x = float(input("x-Abstand = "))
    zKrafte.append((f,x))
'''
    
#Moment um z-Achse
mz = 0
for f,y,z in xKrafte:
    mz += -(f*y)
for f,x in yKrafte:
    mz+= (f*x)

lagerB["Fy"] = -(mz/lagerabstand)
yKrafte.append((lagerB["Fy"],lagerabstand))

my = 0
for f,y,z in xKrafte:
    my+= (f*z)
for f,x in zKrafte:
    my+= -(f*x)
lagerB["Fz"] = (my/lagerabstand)
zKrafte.append((lagerB["Fz"],lagerabstand))


sumy = 0
for f,x in yKrafte:
    sumy += f
lagerA["Fy"] = 0-sumy
yKrafte.append((lagerA["Fy"],0))


sumz = 0
for f,x in zKrafte:
    sumz += f
lagerA["Fz"] = 0-sumz
zKrafte.append((lagerA["Fz"],0))


print("Lager A = ", lagerA)
print("Lager B = ", lagerB)

# Anzeige:

xWerte = []
for i in range(lagerabstand+1): # +1 damit [0-lagerabstand]
    xWerte.append(i)
xWerteOrginal = []
xWerteOrginal = list(xWerte)



# Quwerkrauft y
# insert und so, damit die sprünge gradlienige sien
# heißt es gibt immer zwei werde für den selben x-Wert
erstesMal = True
yWerte = []
fy = 0
i = 0
while i < (len(xWerte)):
    yWerte.append(fy)
    for f,x in yKrafte:
        if x == xWerte[i]: 
            if erstesMal:
                xWerte.insert(i+1,xWerte[i])
                fy += f
                erstesMal = False
            else:
                erstesMal = True
    i+=1
    
    
# Moment z
# Reine y Werte ohne dopplungen 
yWerteOrginal = []
fy = 0
for xWert in xWerteOrginal:
    yWerteOrginal.append(fy)
    for f,x in yKrafte:
        if x == xWert:
            fy += f
mzWerte = []
mzYWert = 0
for x in xWerteOrginal:
            mzYWert += ((1*yWerteOrginal[x])/1000)
            mzWerte.append(round(mzYWert,3))



#X-Achse
xAchse = []
for  x in xWerteOrginal:
    xAchse.append(0)

plt.subplot(2,1,1)
plt.plot(xWerteOrginal,xAchse,color = 'k') # X-Achse
plt.plot(xWerte,yWerte) # Qy
plt.subplot(2,1,2)
plt.plot(xWerteOrginal,mzWerte,color = 'r') # Mz
plt.plot(xWerteOrginal,xAchse,color = 'k') # X-Achse

plt.show()