import time
from zeep import Client
from lxml import etree

client = Client("https://www.pttor.com/Oilprice.asmx?WSDL")
name = ['none']
price = [0]

result = client.service.CurrentOilPrice(Language="en")
root = etree.fromstring(result)
for i in range(len(root)):
    if len(root[i]) == 3:
        name.append(root[i][1].text)
        price.append(float(root[i][2].text))
while True:
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                  Oilprice                                    *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                  Baht to L                                   *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                     Or                                       *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                  L to Baht                                   *")
    print("*                                                                              *")
    print("*                          type exit to leave the program                      *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("********************************************************************************")
    a = input("Select L to Baht or Baht to L (L to Baht is 1 and Baht to L is 2)")
    if a == '1':
        print("********************************************************************************")
        print("*                                                                              *")
        print("*                               Choose type of Oil                             *")
        print("*                                                                              *")
        print("*                               1.  Gasoline 95                                *")
        print("*                                   Price 29.16 Baht                           *")
        print("*                               2.  Gasoline 91                                *")
        print("*                                   Price 25.3 Baht                            *")
        print("*                               3.  Gasohol 91                                 *")
        print("*                                   Price 21.68 Baht                           *")
        print("*                               4.  Gasohol E20                                *")
        print("*                                   Price 20.2 Baht                            *")
        print("*                               5.  Gasohol 95                                 *")
        print("*                                   Price 21.2 Baht                            *")
        print("*                               6.  Diesel                                     *")
        print("*                                   Price 21.1 Baht                            *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("********************************************************************************")
        y = 0
        while not(y in ['1','2','3','4','5','6']) :
        	y = input("Select operations form 1-6 : ") 
        x = float(input("Enter the amount of L : ")) 
        if y == '1':
            print("Gasoline 95")
            z = x*29.16
            print("The total of price is : %0.2f Baht" %z)
        elif y == '2':
            print("Gasoline 91")
            z = x*25.3
            print("The total of price is : %0.2f Baht" %z)
        elif y == '3':
            print("Gasohol 91")
            z = x*21.68
            print("The total of price is : %0.2f Baht" %z)
        elif y == '4':
            print("Gasohol E20")
            z = x*20.2
            print("The total of price is : %0.2f Baht" %z)
        elif y == '5':
            print("Gasohol 95")
            z = x*21.2
            print("The total of price is : %0.2f Baht" %z)
        elif y == '6':
            print("Diesel")
            z = x*21.1
            print("The total of price is : %0.2f" %z)
        elif type(x) == str:
            print("Invalid input") 
        else: 
            print("Invalid input") 
    elif a == '2':
        print("********************************************************************************")
        print("*                                                                              *")
        print("*                               Choose type of Oil                             *")
        print("*                                                                              *")
        print("*                               1.  Gasoline 95                                *")
        print("*                                   Price 29.16 Baht                           *")
        print("*                               2.  Gasoline 91                                *")
        print("*                                   Price 25.3 Baht                            *")
        print("*                               3.  Gasohol 91                                 *")
        print("*                                   Price 21.68 Baht                           *")
        print("*                               4.  Gasohol E20                                *")
        print("*                                   Price 20.2 Baht                            *")
        print("*                               5.  Gasohol 95                                 *")
        print("*                                   Price 21.2 Baht                            *")
        print("*                               6.  Diesel                                     *")
        print("*                                   Price 21.1 Baht                            *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("********************************************************************************")
        w = 0
        while not(w in ['1','2','3','4','5','6']) :
        	w = input("Select operations form 1-6 : ") 
        v = float(input("Enter the amount of baht : ")) 
        if w == '1':
            print("Gasoline 95")
            u = v/29.16
            print("The total of oil is : %0.2f L" %u)
        elif w == '2':
            print("Gasoline 91")
            u = v/25.3
            print("The total of oil is : %0.2f L" %u)
        elif w == '3':
            print("Gasohol 91")
            u = v/21.68
            print("The total of oil is : %0.2f L" %u)
        elif w == '4':
            print("Gasohol E20")
            u = v/20.2
            print("The total of oil is : %0.2f L" %u)
        elif w == '5':
            print("Gasohol 95")
            u = v/21.2
            print("The total of oil is : %0.2f L" %u)
        elif w == '6':
            print("Diesel")
            u = v/21.1
            print("The total of oil is : %0.2f L" %u)
        else:
            print("Invalid input")
    elif a == 'exit': 
        print("********************************************************************************")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                              THANK YOU SO MUCH                               *")
        print("*                              THANK YOU SO MUCH                               *")
        print("*                              THANK YOU SO MUCH                               *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("********************************************************************************")
        break
    else: 
        print("Invalid input") 
    time.sleep(1)
