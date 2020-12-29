#VERİ YAPILARI-DICTIONARY
#OLUŞTURMAAA
#STRING
dictionary ={"reg":"reg model",
             "loj":"lojistik reg",
             "classi":"Random Forest"}
dictionary
len(dictionary)

#NUMBER
dictionary ={"reg":5,
             "loj":78,
             "classi":7}
dictionary

#BİRDEN FAZLA DEĞER
dictionary ={"reg":["RMSE",59],
             "loj":["MSE",78],
             "classi":["DAT",65]}
dictionary

#ELEMAN İŞLEMLERİ

dictionary ={"reg":"reg model",
             "loj":"lojistik reg",
             "classi":"Random Forest"}

dictionary[0]#hatalı
dictionary["reg"]


dictionary ={"reg":["RMSE",59],
             "loj":["MSE",78],
             "classi":["DAT",65]}

dictionary["reg"]
#sözlük içinde sözlük
dictionary ={"reg":{"RMSE":59,
                    "MSE":30,
                    "SSM":80},
             "loj":{"RMSE":40,
                    "MSE":47,
                    "SSM":78},
             "classi":{"RMSE":63,
                    "MSE":52,
                    "SSM":85}}

#eleman bulduk
dictionary["classi"]
dictionary["classi"]["MSE"]

#eleman eklemek->>>>varsa değiştiriyor/yoksa ekliyor
dictionary ={"reg":"reg model",
             "loj":"lojistik reg",
             "classi":"Random Forest"}

dictionary["GBM"] ="gerizekalı bana maldeme"
dictionary

dictionary["reg"] ="değiştirdim seni"
dictionary


dictionary[1] ="yapat sinir ağları"
dictionary

l= [1]
l
dictionary(l) ="yeni bir sey"
dictionary

t =("ali",)
dictionary[t] ="yapat sinir ağları"
dictionary

#tuple'ı key olarak atayabildik.



















