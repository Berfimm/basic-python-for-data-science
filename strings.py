#Strings(tırnak işaretleri sayıları string algılıyor.)
#çarpmak için * ve bir araya getirmek için + kullanmalısın.
"a" + "b"
"a""b"
"a" " b"
"a" "-b"
"a" * 3

#String Method(Fonksiyonlar)
     #LEN (uzunluk)

mvk ="gelecegi_yazanlar"
abe ="gelecegi_yazanlar"
#del abe
a=9
b=10
a*b
len(mvk)

     #Upper()/Lower() Methodu

mvk ="gelecegi_yazanlar"
B=mvk.upper()
B
mvk.lower()

mvk.islower()
mvk.isupper()

B.islower()

     #REPLACE METHODU

mvk ="gelecegi_yazanlar"
mvk.replace("e","a") #1.değiştirmek istediğimiz harf,2.si ise değiştirdiğimiz harf
mvk
#kaydetmek lazım,orijinalinde değişiklik olmadı
mvk.replace("a","i")

     #Karakter Kırpma
mvk =" gelecegi_yazanlar "
mvk.strip() #boşlukları aldı,kırptı
mvk ="*gelecegi_yazanlar*"
mvk.strip()
mvk ="*gelecegi_yazanlar*"
mvk.strip("*") #kırpmak istediğim karakteri yazdım içine!
#all string's methods
dir(mvk)
dir(str) 
mvk ="gelecegi_yazanlar"
mvk.capitalize()
mvk.title()

#SUBSTRING
mvk ="gelecegi_yazanlar"
mvk[0]
mvk[5]
mvk[5:8]#8 den bir önceki
mvk[20]























