n = 2147483647
x = str(bin(n)[2:].zfill(32))
res = ''
for i in range(len(x)):
        if x[i]== '1':
            res += '0'
        else:
            res += '1'
print(res)
print(int(res,2))