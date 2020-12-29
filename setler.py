#VERI YAPILARI -SETLER
# =============================================================================
# #SIRASIZ(INDEXSIZ)
# #TEKRAR EDEN OZELLIKLER YOK
# #DEGISTIRILEMEZLER
# #PERFORMANS ODAKLI
# #ALFABETIK SIRALIYOR
# =============================================================================
s = set()
s
 #liste Uzerinden setler
list =[1,"a","ali",123]
s = set (list)
s

#tuple Uzerinden setler

t =("a","ayso")
s = set(t)
s

ayso ="lutfen bana bakma,uzaya git"
type(ayso)

s =set(ayso)
#sette tek yaziyo,tekrar edenleri tek kabul ediyor.

l =["ali","lütfen","git","git","git"]
s = set(l)
s

len(s)

l[0]
#set nesnesi index islemini destelemiyor.
s[0]

#SETLERDEN ELEMAN EKLEME CIKARMA

list=["beni","aya","yollayan","sana","neler","yapmaz"]
s =set(list)
s

dir(s)
#EKLEME
s.add("ayseyi")
s
s.add("adios babe")
s
#ayni elemanı eklesen dahi,setler eklemiyor.
#DONT WORYYYYYY
s.add("sana")
s

#ELEMAN CIKARMA

s.remove("sana")
s
#eleman yok bulamiyo,hata veriyo
s.remove("sana")
s

#eleman yok,bulamiyo,hata vermiyo

s.discard("sana")
s

#KUME ISLEMLERI
# =============================================================================
# difference() iki kümenin farkı ya da "-" ifadesi
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi
# symetric_difference() ikisinde de olmayanlarÄ±
# =============================================================================

   ############DIFFERENCE##########
set1 =set([1,3,5])
set2 =set([1,2,3])

set1.difference(set2)
set2.difference(set1)
set1-set2
set2-set1
set1.symmetric_difference(set2)


###########INTERSECTION#########

set1 =set([1,3,5])
set2 =set([1,2,3])

#samee
set1.intersection(set2)
set2.intersection(set1)

kesisim = set1&set2
kesisim

#####UNION########
birlesim =set1.union(set2)
birlesim

set1.intersection_update(set2)
set1
############SETLERDE SORGU ISLEMLERI###########

set1 = set([7,8,9,10])

set2 = set([5,6,7,8,9,10])

set1.intersection(set2)
# =============================================================================
# #iki kümenin kesisismi bos mu
# =============================================================================
set1.isdisjoint(set2)

# =============================================================================
# #bir kumenin elemanları baska bir kumede yer aliyor mu
# =============================================================================

set1.issubset(set2)
set2.issubset(set1)


# =============================================================================
# #bir kume diger kumeyi kapsıyor mu kapsamıyor mu
# =============================================================================

set2.issuperset(set1)





