# =============================================================================
# #101 functıons and fonksıyon okur yazarlığı
# =============================================================================

#ekrana yazdıran fonksiyon
print("a","b",sep="_")
print
#fonksiyonun dokumantasyonu
#?print

len("abcdghs")

# =============================================================================
# #FONKSİYON NASIL YAZILIR
# =============================================================================

# =============================================================================
# #  *, /  ,- ,+ ------>>>>> Matematiksel işlemler
# =============================================================================


# =============================================================================
# #x 'e bağlı kare al diyen bir fonksiyon tanımlıyor
# =============================================================================
4**2
def kare_al(x):
    print(x ** 2)
kare_al(3)   

# =============================================================================
# #bilgi notuyla cıktı uretmek(output)
# =============================================================================

def kare_al(x):
    print("Girilen sayının karesi:" + str(x ** 2))
kare_al(3)   

def kare_al(x):
    print("Girilen Sayı:"+ str(x) +" \nGirilen sayının karesi:" + str(x ** 2) )
kare_al(3)   

# =============================================================================
# #iki argümanlı fonksiyon tanımlama
# 
# =============================================================================
def carpma_yap(x, y):
    print("x:" + str(x)+
          "\ny:" + str(y) +
          "\nResult:" + str(x*y))
carpma_yap(5,6)
    
# =============================================================================
#  #On tanımlı argümanlar   
# =============================================================================


def carpma_yap(x, y =6):
    print(x*y)
carpma_yap(3)
    
print("HELLO AI ERA") 
    
#argumanların sıralaması 
    
def carpma_yap(x, y =6):
    print(x*y)
carpma_yap(y=5,x=8)#sırası önemliyse kendin yazabiliyosun
carpma_yap(5,8)#tanımladığın sıraya göre carpar



# =============================================================================
# NE ZAMAN FONKSIYON YAZILIR
#TEKRAR EDEN GÖREVLERİ YERİNE GETİRMEK
# VE VAROLAN İŞLERİ PROGRAMATİK ŞEKİLDE GERÇEKLEŞTİRMEK İÇİN KULLANILIR
# =============================================================================

#SOKAK AYDINLATMA DİREKLERİ,HER BİR LAMBA ISI,NEM,SARJ DURUMU İFADE EDİLSİN   

(40 +25)/ 90 # sadece bir tanesi

def aydınlatma(ısı,nem,sarj):
    print((ısı+nem)/sarj)
aydınlatma(25, 40, 70)
    

# =============================================================================
# #return ---->>>>>>>>>>>>>>çıktıyı kullanabilmek
# =============================================================================

def aydınlatma(ısı,nem,sarj):
   return (ısı+nem)/sarj
output=aydınlatma(25, 40, 70)*9
output
print(output)

def aydınlatma(ısı,nem,sarj):
   return 
   (ısı+nem)/sarj
   
aydınlatma(25, 40, 70)

# =============================================================================
# #local ve global değişkenler
# 
# =============================================================================
#global variables
x=10
Y=50

def carpma_yap(x,y): #local değişkenler/fonksiyonun içinde yer alıyor
    return x*y
carpma_yap(2, 3)


# =============================================================================
# local ve lobal etki alanını değiştirmek
# =============================================================================
#boş listeye eleman eklemek
#ilk local kısma sonra global kısma bakar

x=[]


def eleman_ekleme(y):
     x.append(y)
     print(str(y) +" ifadesi eklendi")
     
     
     
eleman_ekleme(5)
eleman_ekleme("berfo")
eleman_ekleme("merto")
x















































  
    