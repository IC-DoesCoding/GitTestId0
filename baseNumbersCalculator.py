convertList = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
    "G" : 16,
    "H" : 17,
    "I" : 18,
    "J" : 19,
    "K" : 20,
    "L" : 21,
    "M" : 22,
    "N" : 23,
    "O" : 24,
    "P" : 25,
    "Q" : 26,
    "R" : 27,
    "S" : 28,
    "T" : 29,
    "U" : 30,
    "V" : 31,
    "W" : 32,
    "X" : 33,
    "Y" : 34,
    "Z" : 35,

}



while True:
    ip = str(input("Number:")).upper()
    lennum = len(ip)
    charslist=[]
    numValList=[]
    for i in ip:
        charslist.append(i)
    for i in range(lennum):
        #pass
        #print(charslist[(lennum-1)-i])
        numValList.append(convertList[charslist[(lennum-1)-i]])
    #print(charslist)
    bip = input("Base:")
    try:
        bip = int(bip)
    except:
        print("INVALID")


    #print(numValList)
    #print(len(numValList))

    #print(bip)yea
    #ligon
    ans = 0
    for i in numValList:
        ans = ans+(i*(bip**numValList.index(i)))

    print("The answer is : "+str(ans)+"\n\n")
