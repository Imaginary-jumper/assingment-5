list1= []
for i in range(1,11):
    list1.append(i)
print("original list:",list1)
print("extracted first five elements:",list1[0:5])
list1.reverse()
print("reversed extracted elements:",list1[5:])
