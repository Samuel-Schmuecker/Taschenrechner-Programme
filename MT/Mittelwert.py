import math as m

def werteEinlesen()->tuple:
    # returns a tuple withe T and a list withe tuple (u,delta_t) 
    #############################################################
    #Testwerte:
    #SinusSpannung:
    #T,werte = 2,[(230,1),(230,1)]
    #T,werte = 2,[(230,1),(0,1)]

    #RechteckSpannung:
    #T,werte = 80,[(5,20),(10,10),(5,10),(-5,20),(-10,10),(-5,10)]
    #T,werte = 2,[(2,1),(-1,1)]
    #DreiecksSpannung:
    #T,werte = 2,[(3,1),(0,1)]
    #############################################################
    #'''
    T = int(input("Wie lang ist die Periode T? "))
    print("Eigabe der Spannungswerte: ")
    werte = []
    i = 1
    sum_t = 0
    while True:
        if sum_t >= T:
            break
        u = input("U",i," = ")
        if u == "":
            break
        delta_t = input("delta_t",i," = ")

        try:
            u = float(u)
            delta_t = float(delta_t)
            werte.append((u,delta_t))
            i+=1
            sum_t += delta_t
        except:
            print("Nur float Werte!! z.B.: 1.7")
    #'''
    return (T,werte)

def wertBerechnen(T:float, werte:list, form:int)->float:
    #returns a triple (Mittelwert, Gleichrichtwert, Effektivwert). form: 1=Sinus, 2=Rechteck, 3=Dreieck
    if form == 1:
        mittelwert = 0
        gleichrichtwert = 0
        effektivwert = 0
        for u,t in werte:
            flaechePuls = (2*u*t)/m.pi
            mittelwert+= flaechePuls
            gleichrichtwert +=  abs(flaechePuls)
            effektivwert += (u**2*t)/2
        mittelwert = round((1/T)*mittelwert,3)
        gleichrichtwert = round((1/T)*gleichrichtwert,3)
        effektivwert = round((1/T*effektivwert)**0.5,3)
        return (mittelwert, gleichrichtwert, effektivwert)


    elif form == 2:
        faktor = 1
    elif form == 3:
        faktor = 0.5
    
    mittelwert = 0
    gleichrichtwert = 0
    uSpitze = 0

    for u,t in werte:
        mittelwert+= faktor*(u*t)
        gleichrichtwert += faktor*(abs(u)*t)

        if u > uSpitze:
            uSpitze = u
    
    mittelwert = round((1/T)*mittelwert,3)
    gleichrichtwert = round((1/T)*gleichrichtwert,3)

    effektivwert = 0
    for u,t in werte:
        if mittelwert == 0:
            effektivwert += (u**2)*t
        else:
            effektivwert += (u-mittelwert)**2*t
    effektivwert = round((1/T*effektivwert)**0.5,3)
    
    return (mittelwert, gleichrichtwert, effektivwert)

def plotRechteckSpannung(werte:list,mittelwert:float)->None:
    xWerte = [0]
    yWete = [0]

    for i in range(len(werte)):
        if i != 0:
            xWerte.append(i)
            yWete.append(werte[i-1][0])

        xWerte.append(i)
        yWete.append(werte[i][0])

    xWerte.append(len(werte))
    xWerte.append(len(werte))
    yWete.append(werte[len(werte)-1][0])
    yWete.append(0)

    xAchseXY = []
    yMittelwert = []
    for x in xWerte:
        xAchseXY.append(0)
        yMittelwert.append(mittelwert)
        


def plotDreiecksSpannung(wert:list,mittelwert:float)->None:
    xWerte = [0]
    yWete = [0]

    for u,t in wert:
        xWerte.append(t)
        yWete.append(u)
        xWerte.append(t)
        yWete.append(0) 
    
    xWerte.append(len(werte))
    yWete.append(0)

    xAchseXY = []
    yMittelwert = []
    for x in xWerte:
        xAchseXY.append(0)
        yMittelwert.append(mittelwert)
         

while True:
    form = int(input("Ist es eine Sinus-, Rechteck oder Dreiecksspannung? (1,2,3): "))
    if form == 1:
        T,werte = werteEinlesen()
        mittelwert, gleichrichtwert, effektivwert = wertBerechnen(T, werte, form)
        break
    elif form == 2:
        T,werte = werteEinlesen()
        mittelwert, gleichrichtwert, effektivwert = wertBerechnen(T, werte, form)
        plotRechteckSpannung(werte,mittelwert)
        if mittelwert == 0:
            art = "Rechteckwechselspannung"
        else:
            art = "Mischspannung"
        break
    elif form == 3:
        T,werte = werteEinlesen()
        mittelwert, gleichrichtwert, effektivwert = wertBerechnen(T, werte, form)
        plotDreiecksSpannung(werte,mittelwert)
        break
    else:
        print("ungültige Eingabe! 1, 2 oder 3")


print(werte)
print("Mittelwert = ",mittelwert)
print("Gleichrichtwert = ", gleichrichtwert)
print("Effektivwert der Wechselspannung = ", effektivwert)