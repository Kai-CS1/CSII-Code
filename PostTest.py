'''
Created on Sep 12, 2022
@author: KHarashima25
'''
import random

# Begin Program
def main():

    packtype = 1 # set package size to default
    zone = 1 # set zone number to default
    res = '' # set result to none
    price= 0 # set price to default
    multiple=0 # set multiple for packtype and zone

    while True:    
        if packtype == 1:
            res = "3.65,5.9,.007"
            price=.20
            multiple=.03
        if packtype == 2:
            res = "4.3,6.1,.007"
            price=.37
            multiple=.03
        if packtype == 3:
            res = "3.51,10,.016"
            price=.37
            multiple=.04
        if packtype == 4:
            res = "7,12,.26"
            price=.6
            multiple=.05
        if packtype == 5:
            res = "22,18,1"
            price=2.95
            multiple=.25
        if packtype == 6:
            res = "10,12,30"
            price=3.95
            multiple=.35
    
        if zone == 5 and packtype ==6:
            extra = ",99890,05736"
            print(res+extra,"--",price+multiple*5)
            break
        elif zone == 5:
            extra = ",99890,05736"
            print(res+extra,"--",price+multiple*5)
            zone = 1
            packtype = packtype+1
        elif zone == 4:
            extra = ",85610,19899"
            print(res+extra,"--",price+multiple*4)
            zone = zone+1
        elif zone == 3:
            extra = ",20001,98801"
            print(res+extra,"--",price+multiple*3)
            zone = zone+1
        elif zone == 2:
            extra = ",99998,36000"
            print(res+extra,"--",price+multiple*2)
            zone = zone+1
        elif zone == 1:
            extra = ",85000,64000"
            print(res+extra,"--",price+multiple*1)
            zone = zone+1
    exit   
if __name__ == '__main__':
    main()