# =============================================================================
# # =============================================================================
# # DONGULER
# # =============================================================================
 
ogrenci =["ali","veli","berf","mert"]
ogrenci[0]
 
for i in ogrenci: #i'ye ataya ataya ogrencide dönüp dur
    print(i)
     
maaslar=[500,484,4845,56512,56123]
 
for i in maaslar:
     print(i*5)
    
     
def kare_al(x):
   print(x**2)
kare_al


#maaslara %20 zam yapılacak
 
maaslar=[500,484,4845,56512,56123]

for i in maaslar:#donguyle yazdık bunu
    print(i)

#tek tek baktık
maaslar[0]*20/100 +maaslar[0]
maaslar[1]*20/100 +maaslar[0]
maaslar[2]*20/100 +maaslar[0]
maaslar[3]*20/100 +maaslar[0]
maaslar[4]*20/100 +maaslar[0]    

#yeni maasi tanimladik    
def yeni_maas(x):
    print(x)
yeni_maas(4)

#yeni maasi nasil bulacagimizi yazdik
def yeni_maas(x):
    print((x*20)/100 + x)
#denedik    
yeni_maas(1000)
yeni_maas(2000)
yeni_maas(3000)

#listedeki maaslari yazdirdik
for i in maaslar:
    yeni_maas(i)
    
    
    #####MAASA GORE ZAM YAPMAK########
    
maaslar =[1000,2000,3000,4000,5000]  

def maas_ust(x):
    print(x*10/100 +x)
    
def maas_alt(x):
    print(x*20/100 +x)    
    
for i in maaslar:
    if i >= 3000 :
        maas_ust(i)
    else:
        maas_alt(i)
    
    
    
    
    #### BREAK  && CONTINUE #########
    
maaslar =[8000,5000,2000,1000,3000,9000,7000]  
    
#napacagimiza baktik
dir(maaslar)
    
maaslar.sort()    
maaslar    

for i in maaslar:   
    if i ==3000 :
        print("kesildi")
        break
    print(i)
    
    
for i in maaslar:   
    if i ==3000 :
       
        continue
    print(i)  
    
# =============================================================================
# WHILEEEEEEE
# =============================================================================

sayi =8

while sayi < 10:
    sayi +=1
    print(sayi)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    