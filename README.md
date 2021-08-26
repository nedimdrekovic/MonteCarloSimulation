
# Berechnung von PI mit der MonteCarlo Simulation

Bei diesem Projekt handelt es sich um eine einfache Visualisierung zur probabilistischen Berechung der Kreiszahl Pi. Hierbei handelt es sich um einen Monte Carlo Simulation (https://de.wikipedia.org/wiki/Monte-Carlo-Simulation).

# Funktionsweise des Algorithmus
1) Generiere eine beliebige Anzahl an Punkten zufällig im Bereich des Quadrats.
2) Berechne mithilfe des Satzes des Pythagoras ob die generierten Punkte im Kreis liegen.
3) Das Verhältnis der Anzahl der im Kreis liegenden Punkte zu der Gesamtzahl aller Punkte ergibt ~ π/4

## Pseudocode
```javascript
function approximiere_pi(punkteInsgesamt)

    punkteImKreis := 0   // Zählt die Punkte innerhalb des Kreises

    // So oft wiederholen, wie es Punkte gibt:
    for i := 1 to punkteInsgesamt do

        // Zufälligen Punkt im Quadrat [0,0] bis (1,1) erzeugen
        x := random(0.0 ..< 1.0)
        y := random(0.0 ..< 1.0)

        // Wenn der Punkt innerhalb des Kreises liegt ...
        if x * x + y * y <= 1.0
            punkteImKreis++   // Zähler erhöhen

    return 4.0 * punkteImKreis / punkteInsgesamt
```
# Weiteres

Durch Erhöhung des Stichprobenumfangs (= die zu generierenden Punkte) wird π präziser (gegeben durch Gesetz der großen Zahlen).

<p float='left'>
    <img src="https://user-images.githubusercontent.com/73491052/128614754-acf1a2fc-908c-4579-9d62-96185b1050f9.png" width=255 align=left>
    <img src="https://user-images.githubusercontent.com/73491052/128614396-274c2c82-f8f9-4099-9812-1177c954f53d.png" width=255 align=left>
    <img src="https://user-images.githubusercontent.com/73491052/128614395-03e689c0-68f5-4a52-904f-fbe673954b47.png" width=255 align=left>
</p>







<br></br>
