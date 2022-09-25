
list1 = []
with open('test', 'r') as file:
    list1 = file.readlines()
list = []
for i in list1:
    list.append(i.split('\n')[0])

print(list)
print( 'test8' in list)