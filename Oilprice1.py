import time
while True:
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                               ป้ายราคาน้ำมัน                                    *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                               เลือกบาทต่อลิตร                                  เ*")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                    หรือ                                       *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                               เลือกลิตรต่อบาท                                  เ*")
    print("*                                                                              *")
    print("*                                                                              *")
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
        print("*                               เลือกชนิดน้ำมัน                                    *")
        print("*                                                                              *")
        print("*                               1.  Gasoline 95                                *")
        print("*                                   ราคา 29.16 บาท                             *")
        print("*                               2.  Gasoline 91                                *")
        print("*                                   ราคา 25.3 บาท                              *")
        print("*                               3.  Gasohol 91                                 *")
        print("*                                   ราคา 21.68 บาท                             *")
        print("*                               4.  Gasohol E20                                *")
        print("*                                   ราคา 20.2 บาท                              *")
        print("*                               5.  Gasohol 95                                 *")
        print("*                                   ราคา 21.2 บาท                              *")
        print("*                               6.  Diesel                                     *")
        print("*                                   ราคา 21.2 บาท                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("********************************************************************************")
        y = int(input("Select operations form 1-6 : "))
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
            z = x*21.2
            print("The total of price is : %0.2f" %z)
        elif type(x) == str:
            print("Invalid input") 
        else: 
            print("Invalid input") 
    elif a == '2':
        print("********************************************************************************")
        print("*                                                                              *")
        print("*                               เลือกชนิดน้ำมัน                                    *")
        print("*                                                                              *")
        print("*                               1.  Gasoline 95                                *")
        print("*                                   ราคา 29.16 บาท                             *")
        print("*                               2.  Gasoline 91                                *")
        print("*                                   ราคา 25.3 บาท                              *")
        print("*                               3.  Gasohol 91                                 *")
        print("*                                   ราคา 21.68 บาท                             *")
        print("*                               4.  Gasohol E20                                *")
        print("*                                   ราคา 20.2 บาท                              *")
        print("*                               5.  Gasohol 95                                 *")
        print("*                                   ราคา 21.2 บาท                              *")
        print("*                               6.  Diesel                                     *")
        print("*                                   ราคา 21.2 บาท                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("*                                                                              *")
        print("********************************************************************************")
        w = int(input("Select operations form 1-6 : "))
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
            u = v/21.2
            print("The total of oil is : %0.2f L" %u)
        else:
            print("Invalid input") 
    else: 
        print("Invalid input") 
    time.sleep(1)
