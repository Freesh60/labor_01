#számológép
print("Számológép")

szam1 = input("Kérem az első számot: ")
while not szam1.isnumeric():
    print("Rossz érték!!!!")
    szam1 = input("Kérem az első számot: ")

muvelet = input("Milyen művelet legyen(+,-,*,/): ")
