#jövedelemszámítás
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
gyerek = ""
if kor > 25:
    gyerek = input("Van 3 gyereked és nő vagy (igen/nem)?")
brutto = int(input("Mennyi a bruttó jövedelmed?"))
if kor <= 25 or gyerek in ["igen", "Igen", "i", "I"]:
    if brutto > 500000:
        szja = (brutto-500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

print("SZJA:".ljust(20, "_"), str(int(szja)).rjust(10, "_"), sep="")
print("Nyugdíj:".ljust(20, "_"), str(int(brutto * 0.1)).rjust(10, "_"), sep="")
print("EÜ:".ljust(20, "_"), str(int(brutto * 0.07)).rjust(10, "_"), sep="")
print("Munkanélküli:".ljust(20, "_"), str(int(brutto * 0.015)).rjust(10, "_"), sep="")
print("\nNetto:".ljust(20, "_"), str(int(brutto - (brutto * 0.185) - szja)).rjust(10, "_"), sep="")
