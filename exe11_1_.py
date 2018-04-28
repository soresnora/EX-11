def exe11():
    szlist=[]
    for i in range(10,100):
        for j in range(10,100):
            sz = i*j
            if sz==sz[::-1]:
                szlist.append(sz)
    print(szlist)

exe11()