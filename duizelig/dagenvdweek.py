dag1 = 'Maandag'
dag2 = 'Dinsdag'
dag3 = 'Woensdag'
dag4 = 'Donderdag'
dag5 = 'Vrijdag'
dag6 = 'Zaterdag' 
dag7 = 'Zondag' 
dagen = [dag1,dag2,dag3,dag4,dag5,dag6,dag7]
GekozenDagNummer = int(input("""kies een dag met gebruik van een getal
Maandag = 0
disndag = 1
woensdag = 2 
donderdag = 3 
vrijdag = 4
zaterdag = 5
zondag = 6 \n"""))
dagnummer = 0
while dagnummer<= 6 and GekozenDagNummer >= dagnummer:
    print(dagen[dagnummer])
    dagnummer = dagnummer + 1


