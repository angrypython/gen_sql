"""Отсортируйте словарь по значению в порядке возрастания и убывания."""
import datetime
import time

a = dict()
c = dict()
b =range(1, 10)
#timestart = datetime.datetime.today()
#print(timestart.strftime("%d-%m-%Y-%H:%M:%S.%f"))
for i in b:
    a['a'+ str(i)] = i
    c['b'+ str(i)] = i
#timestart = datetime.datetime.today()

for i in c:
    print(i)
    a[i] = c[i]
print(a)

#print(timestart.strftime("%d-%m-%Y-%H:%M:%S.%f"))
#print(sorted(a.items(), reverse=True))