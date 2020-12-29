##Fonksiyonlar dilin bas tacidir.
##Birinci sinif nesnelerdir
##Yan etkisiz fonksiyonlar vardir.(stateless,girdi-cikti)
#Yuksek seviye fonksiyonlardir
#Vektorel operasyonlardir


# =============================================================================
# ##Yan etkisiz fonksiyonlar vardir.(stateless,girdi-cikti)
# =============================================================================
#Ornek1
#bağımlı (A'ya)
A =5
def impure_sum(a):
    return a + A
impure_sum(5)

#bağımsız
def pure_sum(a,b):
    return a+ b
pure_sum(5, 7)

#Ornek2:Olumcul yan etkiler///Dosyadan cektik

#bagimli fonksiyonlar
class LineCounter:
    def __init__(self,filename):
        self.file =open(filename, "r")
        self.lines =[]
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
lc =LineCounter("deneme.txt")

print(lc.lines)
print(lc.count())

lc.read()####dosya okuma islemini yapmadan bos ve 0 geliyordu.OOP



print(lc.lines)
print(lc.count())


#FP-functional programming
#bagimsiz fonksiyonlar
def read(filename):#dosyayı açtık
    with open(filename , "r") as f :
        return [line for line in f]
def count(lines):
    return  len(lines)
example_lines =read("deneme.txt")
lines_count =count(example_lines)
lines_count

        
# =============================================================================
# Unnamed-function //LAMBDA//
# =============================================================================

#isimli
def old_sum(a,b):
    return a+b
old_sum(6,8)

new_sum = lambda a,b : a +b #def
new_sum(6, 9)

sirasiz_liste = [("a" , 15), ("b" , 4), ("c" , 5), ("d" ,12)]
sirasiz_liste

#listedeki her elemanin ikinci elemanina gitti ve siraladı
sorted(sirasiz_liste , key =lambda x : x[1])


# =============================================================================
# #Vektorel islemler
# =============================================================================

#CARPMA ISLEMI(oop)---------->>>>>dongu
a = [1,4,5,6]
b = [4,5,6,7]

ab = [] #sonuclari saklamak icin yeni liste
range(0,len(a)) #a'nin icinde gezinicek(aralik ve uzunluk)

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
    
ab

#FP ---------->>>>numpppyyyyyyyyyyyyyyyy

import numpy as np  #------>>>>>matematiksel islemler

a = np.array([1,4,5,6])
b = np.array([4,5,6,7])

a*b

# =============================================================================
# MAP/FILTER/REDUCE
# 
# =============================================================================
import numpy as np
liste = [1,2,3,4,5]

for i in liste:
    print(i+10)

#map(vektorel operasyon) yapisi ve lambda mimarisi

list(map(lambda x:x+10,liste))


#filter(isteneni getiriyor)
liste =[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 ==0 , liste))

#reduce(tek deger)

from functools import reduce

liste = [1,2,3,4]

reduce(lambda a,b :a+b, liste)

# =============================================================================
# 
# #MODUL OLUSTURMA
# KUTUPHANE,MODUL,PAKET
# belirli amaclari yerine gitrmek icin kullanillir
# =============================================================================

def yeni_maas(x):
    print((x*20)/100 + x)
    
maaslar =[100,2000,3000,4000,6000]

#baska dosyadan
#Fonksiyon cagirdik
import HesapModulu
HesapModulu.yeni_maas(1000)




import HesapModulu as hm
hm.yeni_maas(1000)



from HesapModulu import yeni_maas
yeni_maas(444)



import HesapModulu as hm
hm.maaslar


##Exceptionssss
#except yapisi hatayi es gecer

a = 10
b = 0

a/b #(ZeroDevisionError)



try :
    print(a/b)
except ZeroDivisionError:
    print("Paydada sıfır olmaz")


#tip hatasi

a= 10
b= "5"

a/b


try:
    print(a/b)
except(TypeError):
    print("Sayi ve string problemi")


#no error
a= 10
b= 5

a/b


try:
    print(a/b)
except(TypeError):
    print("Sayi ve string problemi")












