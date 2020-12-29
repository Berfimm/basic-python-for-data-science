# =============================================================================
# #OBJECT ORIENTED PROGRAMMING
# =============================================================================

#CLASS YAPILARI(benzer ozellikler,aynı amaclar)

class VeriBilimcii():
    print("Bu bir sınıftır")

#########Class attrıbutes######

class VeriBilimci():
    bolum = "CS"
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []

#siniflarin ozelliklerine eristik
VeriBilimci.bolum
VeriBilimci.sql
VeriBilimci.deneyim_yili

#siniflerin özelliklerini değiştirmek
VeriBilimci.sql ="Hayir"
VeriBilimci.sql

#intantiation-örnekleme

berf = VeriBilimci()
berf.sql
berf.bolum

#ekleme
berf.bildigi_diller.append("java")
berf.bildigi_diller


mert =VeriBilimci()
mert.bildigi_diller


# =============================================================================
# #ornek ozellikleri--->>>
# #her bi ornegin kendi icinde degisen ozelliklerden olusabildigini gostermektir
# # __init__ --->>
# #self ----->>ornekleri temsil eder
# =============================================================================

class VeriBilimci ():
    bildigi_diller = ["R","PYTHON"] #class değkenleri
    def __init__(self): #her ornek ifadesi tmesil eder
        self.bildigi_diller =[]

berf =VeriBilimci()
berf.bildigi_diller
berf.bildigi_diller.append("python")

mert =VeriBilimci()
mert.bildigi_diller.append("R")
mert.bildigi_diller

VeriBilimci.bildigi_diller

#ORNEK METODLAR

class VeriBilimci ():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller =[]
        self.bolum =''
        
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
        
berf = VeriBilimci()
berf.bildigi_diller
berf.bolum

mert = VeriBilimci()
mert.bildigi_diller
mert.bolum

dir(VeriBilimci)

berf.dil_ekle("python")
berf.bildigi_diller

mert.dil_ekle("java")
mert.bildigi_diller
















