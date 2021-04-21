n = int(input())
hh = n // 3600
if hh < 10:
    hh = str("0" + str(hh))
mm = n // 60 - int(hh) * 60
if mm < 10:
    mm = str("0" + str(mm))
ss = n % 60
if ss < 10:
    ss = str("0"+str(ss))
print(str(hh), str(mm), ss, sep=':')
