'''
@author: KHarashima25
This code allows you to get the shipping price of mail from the input of length, height, width, starting and ending zips
Created on Sep 12, 2022
Last Edited on Oct 3, 2022
Bugs:
Function getSize is weird, doesn't work for some reason
'''
def main():
    query = input("Please type in the following information about your package, seperated by commas.\n- length\n- height\n- width\n- starting zip code\n- ending zip code\n") # query user for package data
    query = query.replace(' ', '')                          # clean results
    answer = query.split(',')                               # split results into list / array
    length = getLength(answer)                              # seperate and troubleshoot length
    height = getHeight(answer)                              # seperate and troubleshoot height
    width = getWidth(answer)                                # seperate and troubleshoot width
    zip1, zip2 = getZips(answer)                            # seperate and troubleshoot zips
    packtype = getPackage(length, width, height)            # get package type from proportions
    distance = getDistance(zip1, zip2)                      # get distance (zones travelled through) from zips
    price = getPrice(packtype, distance)                    # get price from packtype and distance
    print(price)                                            # Print price for user
  
def getLength(answer): # seperate and troubleshoot length
    try:
        length = answer[0]      # seperate length from list
        length = float(length)  # convert length to float
    except:
        length = input("Your input for length was incorrect. Please retype package length:\n")  # try catch - fail loop
    return(length)              # return length as float
def getHeight(answer):          # seperate and troubleshoot height
    try:
        height = answer[1]      # seperate height from list
        height = float(height)  # convert height to float
    except:
        height = input("Your input for height was incorrect. Please retype package height:\n")  # try catch - fail loop
    return(height)              # return height
def getWidth(answer):           # seperate and troubleshoot width
    try:
        width = answer[2]       # seperate width from list
        width = float(width)    # convert width to float
    except:
        width = input("Your input for width was incorrect. Please retype package width:\n")     # try catch - fail loop
    return(width)               # return width
def getZips(answer):            # seperate and troubleshoot zips
    try:
        zip1 = answer[3]        # seperate starting zip from list
        while True:             # loop
            if len(zip1) == 5:  # test for if real zip
                zip1 = int(zip1)# convert zip to int
                break           # break to escape
            else:
                zip1 = input("Your input for starting zip was incorrect. Please retype zip:\n") # try catch - fail loop
    except:
        zip1 = input("Your input for starting zip was incorrect. Please retype zip:\n")         # try catch - fail loop
    try:
        zip2 = answer[4]        # seperate ending zip from list
        while True:             # loop
            if len(zip2) == 5:  # test for if real zip
                zip2 = int(zip2)# convert zip to int
                if zip2 == zip1:# test for if zip1 and zip2 identical
                    zip2 = input("Your input for ending zip is the same as starting zip. Please retype zip:\n") # try catch - fail loop
                else:
                    break       # break to escape
            else:
                zip2 = input("Your input for ending zip was incorrect. Please retype zip:\n")   # try catch - fail loop
    except:
        zip2 = input("Your input for ending zip was incorrect. Please retype zip:\n")           # try catch - fail loop
    return(zip1, zip2)          # return zips
    
def getPackage(length, width, height):  #description-gets package type from proportions given, #length width and height are the proportions used, #packtype = returned value for the type of package
    while True:                         # loop for errors
        packtype = ''                   # final result
        prop = length+height+width      # variable for packages to test
        prop = prop*2                   # variable for packages to test
        if length >= 3.5 and length <= 4.25 and height >= 3.5 and height <= 6 and width >= .007 and width <= .016:
            print("Your mail is a regular post card")
            packtype = 'postcard1'
        elif length >= 4.25 and length <= 6 and height >= 6 and height <= 11.5 and width >= .007 and width <= .015:
            print("Your mail is a large post card")
            packtype = 'postcard2'      
        elif length >= 3.5 and length <= 6.125 and height >= 5 and height <= 11.5 and width >= .016 and width <= .25:
            print("Your mail is a regular envelope")
            packtype = 'envelope1' 
        elif length >= 6.125 and length <= 24 and height >= 11 and height <= 18 and width >= .25 and width <= .5:
            print("Your mail is a large envelope")
            packtype = 'envelope2'   
        elif prop <= 84 and height > 11 and length > 6.125 and width > .25:
            print("Your mail is a normal package")
            packtype = 'pack1'
        elif prop >= 84 and prop <= 130 and height > 11 and length > 6.125 and width > .25:
            print("Your mail is a large package")
            packtype = 'pack2'    
        elif prop > 130:
            print("Your mail is too large - Unmailable")    # unmailable
            main()
        else:
            print("Your mail is unmailable, does not fit proportions")    # unmailable
            main()
        if packtypoe == 'postcard1' or packtype == 'postcard2' or packtype == 'envelope1' or packtype == 'envelope2' or packtype == 'pack1' or packtype == 'pack2': #test for if success
            break
    return packtype

def getDistance(zip1, zip2):                    # Get the zones the package must travel through
    zone1 = 0                                   # get zip1 through if chain
    if zip1 >= 1 and zip1 <= 6999:
        zone1 = 1
    elif zip1 >= 7000 and zip1 <= 19999:
        zone1 = 2
    elif zip1 >= 20000 and zip1 <= 35999:
        zone1 = 3
    elif zip1 >= 36000 and zip1 <= 62999:
        zone1 = 4
    elif zip1 >= 63000 and zip1 <= 84999:
        zone1 = 5
    elif zip1 >= 85000 and zip1 <= 99999:
        zone1 = 6
    zone2 = 0                                   # get zip2 through if chain
    if zip2 >= 1 and zip2 <= 6999:
        zone2 = 1
    elif zip2 >= 7000 and zip2 <= 19999:
        zone2 = 2
    elif zip2 >= 20000 and zip2 <= 35999:
        zone2 = 3
    elif zip2 >= 36000 and zip2 <= 62999:
        zone2 = 4
    elif zip2 >= 63000 and zip2 <= 84999:
        zone2 = 5
    elif zip2 >= 85000 and zip2 <= 99999:
        zone2 = 6
    distance = zone2 - zone1    # get difference
    distance = abs(distance)    # remove negatives
    return distance             # return distance

def getPrice(packtype, distance): # get total price with package type and distance
    if packtype == 'postcard1':
        price = .20 + distance *.03
    elif packtype == 'postcard2':
        price = .37 + distance *.03
    elif packtype == 'envelope1':
        price = .37 + distance *.04
    elif packtype == 'envelope2':
        price = .60 + distance *.05
    elif packtype == 'pack1':
        price = 2.95 + distance *.25
    elif packtype == 'pack2':
        price = 3.95 + distance *.35
    return(price) # return price

if __name__ == '__main__':
    main()