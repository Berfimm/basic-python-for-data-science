#####MIRAS YAPILARI########
#bir class baska classin ozelliklerini kapsıyorsa,
#yani o classın ozelliklerini kullanabiliyorsak



#calısanlar ve departmanlar
class  Employees():
    def __init__(self):
        self.FirstName = " "
        self.LastName = " "
        self.Address = ""

class  DataScience(Employees):
    def __init__(self):
        self.Programming = " "
       
        
class  Marketing(Employees):
    def __init__(self):
        self.StoryTelling = " "
       
        
veribilimci1 =DataScience()
veribilimci1.Programming

#fonksiyonel yapı
class  Employees_new():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
berf = Employees_new("berf", "fdad", "sadsad")
berf.Address
