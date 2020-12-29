#MINI UYGULAMA
sinir = 11245
magaza_adi = input("Please enter your name: ")
gelir = int(input("please enter your revenue: "))

if  gelir < sinir :
    print("Sorryy " +  magaza_adi +  " kapatılacaktır" )
    
elif gelir == sinir :
    print("can rise!! "+  magaza_adi)
else:
    print(" will close!!! "+  magaza_adi)