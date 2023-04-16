a=5000
b=1000
c=600
d=100
prod_max=7000
prod_min=2000
pmt=int(input("Masukan jumlah permintaan: "))
psd=int(input("Masukan jumlah persediaan: "))

#Variabel Permintaan
if pmt<=b:
    turun=1
    print("Derajat Keanggotaan pmt turun: ",turun)
elif pmt>=b and pmt<=a:
    turun=(a-pmt)/(a-b)
    print("Derajat keanggotaan pmt turun= ",turun)
elif pmt>=a:
    turun = 0
    print("Derajat keanggotaan pmt turun=", turun)

if pmt<=b:
    naik=0
    print("Derajat Keanggotaan pmt naik: ",naik)
elif pmt>=b and pmt<=a:
    naik=(pmt-b)/(a-b)
    print("Derajat keanggotaan pmt naik= ",naik)
elif pmt>=a:
    naik = 1
    print("Derajat keanggotaan pmt naik=", naik)

#Variabel Persediaan
if psd<=d:
    sedikit=1
    print("Derajat Keanggotaan psd sedikit: ",sedikit)
elif psd>=d and psd<=c:
    sedikit=(c-psd)/(c-d)
    print("Derajat keanggotaan psd sedikit= ",sedikit)
elif psd>=c:
    sedikit=0
    print("Derajat Keanggotaan psd sedikit: ",sedikit)

if psd<=d:
    banyak=0
    print("Derajat Keanggotaan psd banyak: ",banyak)
elif psd>=d and psd<=c:
    banyak=(psd-d)/(c-d)
    print("Derajat keanggotaan psd banyak= ",banyak)
elif psd>=c:
    banyak=1
    print("Derajat Keanggotaan psd banyak: ",banyak)

def Rule1():
    prod_brg_bertambah1=min(naik,banyak)
    return prod_brg_bertambah1

def Rule2():
    prod_brg_berkurang1=min(turun,sedikit)
    return prod_brg_berkurang1
#Rule 3 : IF Permintaan SEDIKIT And Persediaan BANYAK THEN Produksi Barang BERKURANG"
def Rule3():
    prod_brg_berkurang2=min(turun,banyak)
    return prod_brg_berkurang2

def Rule4():
    prod_brg_bertambah2=min(naik,sedikit)
    return prod_brg_bertambah2

z1 = (Rule1()*(prod_max-prod_min))+prod_min
z2 = prod_max-(Rule2()*(prod_max-prod_min))
z3 = prod_max-(Rule3()*(prod_max-prod_min))
z4 = (Rule4()*(prod_max-prod_min))+prod_min

print("Z akhir dengan merata-rata semua z berbobot")
z=round(((Rule1()*z1)+(Rule2()*z2)+(Rule3()*z3)+(Rule4()*z4))/(Rule1()+Rule2()+Rule3()+Rule4()))
print("z=","(",Rule1(),"",z1,")+(",Rule2(),"",z2,")+(",Rule3(),"",z3,")+(",Rule4(),"",z4,"))/(",Rule1(),"+",Rule2(),"+",Rule3(),"+",Rule4(),"))")
print("Jadi jumlah makanan yang harus diproduksi sebanyak",z,"kemasan")