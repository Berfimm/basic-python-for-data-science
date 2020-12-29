#VERI YAPILARI
#LISTELER-DEGISTIRILEBILIR
#[]
#list[]

notlar = [70,80,90,100]
type(notlar)

list = ["a",19.4,90]
list_genis = ["a",19.4,90 ,notlar]
len(list_genis)
type(list_genis[0])
type(list_genis[1])
type(list[2])


all_array=[list,list_genis]
#del list
#LISTE ELEMANLARINA ERISMEK
list =[10,20,50,0]
list[0]
list[1]
list[5]

#boşluk sıfırıncı eleman yada sonuncu eleman demek
list[0:2]
list[:2]
list[2:]


new_list=["a",10,20,[20,40,60]]
new_list
 
new_list[0:3]
new_list[2]
new_list[3][1]
new_list[3][2]

#LISTELERDE ELEMAN DEĞİŞTİRME SİLME

list =["ali","veli","memo","ayse"]
list

list[1]
list[1]= "velinin anası" #atama yaptık
list

list[0:4]=["berfo","büşo","ayso","fato"]
list

#listeye eleman ekleme
list =["ali","veli","memo","ayse"]
list +["kemal"]#eklendi ama kalıcı değil
list =list +["kemal"]#eklendi ve kalıcı
list

#listeden eleman silme
#del list[1]
list

list =["fato","kado","şilo"]
dir(list)
#APPEND
list.append("salo")
list

#REMOVE
list.remove("salo")
list

#INSERT (KALICI ELEMAN EKLEME)
list =["fato","kado","şilo"]
list.insert(0, "ayso")
list
list[0] = "ayse"
list
list.insert(2, "mehmet")
list
list.insert(5, "berf")
list
len(list)
list.insert(len(list), "merto")
list

#POP(KALICI ELEMAN SİLME)

list.pop(5)
list
#COUNT(SAYMA)
list = ['ayse', 'berf', 'mehmet', 'kado', 'şilo', 'berf', 'merto']
list.count("berf")
list.index("ayse")
#COPY

list_yedek = list.copy()

#EXTEND
list.extend(["a","b",10])
list

#INDEX

list.index("ayse")


#REVERSE 
list.reverse()
list

#SORT (SIRALAMA)
list = [ 'b', 'a', 'merto', 'berf', 'şilo', 'kado', 'mehmet', 'berf', 'ayse']
list.sort()
list

list = [5,6,7,1,0,8,95]
list.sort()
list
 #CLEAR
list.clear()
list










