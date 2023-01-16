
s = 0
for i in range(50):
    code=str(i).zfill(6)
    url="https://fund.eastmoney.com/pingzhongdata/"+code+".js"
    print (url)
