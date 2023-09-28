#számológép

def adatkeres():
    szam = input("Kérem az első számot: ")
    while not szam.isnumeric():
        print("Rossz érték!!!!")
        szam = input("Kérem az első számot: ")
    szam = int(szam)
    return szam

#program indítás
print("Számológép")
szam1 = adatkeres()

muvelet = input("Milyen művelet legyen(+,-,*,/): ")
while muvelet not in {"+","-","*","/"}:
    print("Nem jó a műveleti jel!!!!")
    muvelet = input("Milyen művelet legyen(+,-,*,/): ")

szam2 = adatkeres()

eredmeny = 0
if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2

print(str (szam1).rjust(50))
print(muvelet, end="")
print(str (szam2).rjust(49))
print("_".rjust(50, "_"))
print(str(eredmeny).rjust(50))

