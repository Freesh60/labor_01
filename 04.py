#számológép
print("Számológép")

szam1 = input("Kérem az első számot: ")
while not szam1.isnumeric():
    print("Rossz érték!!!!")
    szam1 = input("Kérem az első számot: ")
szam1 = int(szam1)

muvelet = input("Milyen művelet legyen(+,-,*,/): ")
while muvelet not in {"+","-","*","/"}:
    print("Nem jó a műveleti jel!!!!")
    muvelet = input("Milyen művelet legyen(+,-,*,/): ")

szam2 = input("Kérem a második számot: ")
while not szam2.isnumeric():
    print("Rossz érték!!!!")
    szam2 = input("Kérem a második számot: ")
szam2 = int(szam2)

if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2
