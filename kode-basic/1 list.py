# INI LIST
# LIST

list = [1, 3 ,2 ,4]
print(list)
print(list + [5, 6])
print(list *5)
list.append(9)
print(list)

list.append([5,6]) 
print(list)

list = [1,2,3]
list.extend([4,5,'enam'])
print(list)

list.remove('enam')
print(list)

list2 = [1,2,3,[4,5]]
list2.remove([4,5])
print(list2)