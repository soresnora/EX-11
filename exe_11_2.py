def exe11():
    for i in range(100,10,-1):
        for j in range(100,10,-1):
            sz = i*j
            if str(sz)==str(sz)[::-1]:
                palind=sz
                x1=i
                x2=j
                return '{0}*{1}={2}'.format(x1,x2,palind)

print(exe11())