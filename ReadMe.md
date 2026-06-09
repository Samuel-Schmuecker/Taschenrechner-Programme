# Dokumentation der MicroPython-MessTechnikProgramme (Casio fx-9860GIII)

## 1. A_D_Wndl.py 
Programm zur Berechnung der wichtigsten Kenngrößen eines A/D-Wandlers.

**Eingabe:** 
* n (Anzahl der Bits)
* mb (Messbereich, z. B. +/- Volt)

**Ausgabe:**
* Quantisierungsstufe $Q$ ($U_{LSB}$)
* Maximaler Quantisierungsfehler $F_{max}$

**Eingabe für Messung:** 
* x (Spezifischer Messwert) 

**Ausgabe:**
* Digitaler Ausgabewert des A/D-Wandlers (Dezimal)
* Bitkombination (Binärwert)
* Absoluter Quantisierungsfehler $F$

---

## 2. gaus_Fehler.py
Programm zur statistischen Auswertung von Messreihen ("Gaußscher Fehler").

**Eingabe:** 
* anzahl (Anzahl der Messwerte)
* xn (Einzelne Messwerte)

**Berechnete Kenngrößen:**
* Arithmetischer Mittelwert
* Standardabweichung $s$
* Standardabweichung des Mittelwertes $u$ (Standardmessunsicherheit)
* Vertrauensbereich / Vertrauensintervall des Mittelwertes

**Eingabe für statistische Sicherheit:** 
* sicherheit (Auswahl der Sicherheitsstufe 0–4 für Prozentwerte)

**Ausgabe:**
* Anwendung des Student-t-Faktors (falls Stichprobenanzahl klein)
* Relativer Fehler $f$ in %

---

## 3. gaus_Ver.py 
Programm zur Bestimmung der Gaußschen Normalverteilung und der Quantile.

**Eingabe:** * xMittel (Mittelwert $\mu$)
* u (Standardabweichung $\sigma$)
* xo (Obergrenze)

**Berechnete Kenngrößen (Obergrenze):**
* Quantil $z$
* Zugehöriger $\alpha$-Wert (Tabellenwert)
* Wahrscheinlichkeit für Werte < Obergrenze: $P(X < x_o)$

**Eingabe für Intervall:** 
* xu (Untergrenze)

**Berechnete Kenngrößen (Untergrenze & Intervall):**
* Quantil $z$ für die Untergrenze
* Zugehöriger $\alpha$-Wert (Tabellenwert)
* Wahrscheinlichkeit für Werte > Untergrenze: $P(X > x_u) $
* Wahrscheinlichkeit für Werte zwischen Ober- und Untergrenze: $P(x_u \le X \le x_o)$

---

## 4. ind_R_Me.py
Programm zur Berechnung der korrigierten Werte bei der indirekten Widerstandsmessung (strom- oder spannungsrichtige Schaltung).

**Eingabe:** 
* Schaltungsart (Stromrichtig / Spannungsrichtig)
* Umess (Gemessene Spannung)
* Imess (Gemessener Strom)
* Ri (Innenwiderstand des jeweiligen Messgerätes: $R_{iA}$ oder $R_{iV}$)

**Ausgabe aller Kennwerte:**
* $R_{iA}$ [Ohm] oder $R_{iV}$ [Ohm]
* $U_m$ [V] (Gemessene Spannung)
* $I_m$ [A] (Gemessener Strom)
* $R_m$ [Ohm] (Scheinbarer Widerstand aus den Messwerten, R mit Fehler)
* Absolute Schaltungsabweichung $F$ [Ohm]
* Relative Schaltungsabweichung $f$ [%]
* $R$ [Ohm] (Wahrer, korrigierter Widerstand)

---

## 5. MesBerw.py
Programm zur Messbereichserweiterung (Bestimmung der notwendigen Widerstände).

**Eingabe:** 
* Betriebsart (Amperemeter oder Voltmeter)
* Um (Spannung bei Vollausschlag)
* Im (Strom bei Vollausschlag)

**Berechnete Kenngrößen:**
* Innenwiderstand $R_i$ [Ohm] des Messwerks

**Eingabe Ziel-Messbereich:** 
* Zielwert, auf den erweitert werden soll (Gesamtspannung oder Gesamtstrom)

**Ausgabe:**
* Notwendiger Shuntwiderstand $R_n$ (Parallelwiderstand bei Amperemeter) oder Vorwiderstand $R_v$ (bei Voltmeter) [Ohm]

---

## 6. Mittelwert.py
Programm zur mathematischen Analyse periodischer Spannungsverläufe.
*(Hinweis: Plot-Methoden sind nicht berücksichtigt, da diese auf dem Taschenrechner mangels Bibliotheken nicht funktionieren).*

**Eingabe:** 
* Spannungsverlauf / Signalform (z. B. Rechteck, Sägezahn)
* T (Periodendauer)
* $u_n$ / $delta_n$ (Teilspannungen und zugehörige Zeitabschnitte)

**Ausgabe:**
* Arithmetischer Mittelwert (Gleichanteil)
* Gleichrichtwert (Linearer Mittelwert der Betragswerte)
* Effektivwert (RMS-Wert) der Wechselspannung / Mischspannung