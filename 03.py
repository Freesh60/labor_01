#jövedelemszámítás
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
#gyerek = input("Van 3 gyereked és nő vagy?")
brutto = int(input("Mennyi a bruttó jövedelmed?"))
if kor <= 25:
    szja = 0
else:
    szja = brutto * 0.15

print("SZJA: ", szja)
