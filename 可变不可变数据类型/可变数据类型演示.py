a = [1,2,3]
print(id(a))
a[1] = 5

print(id(a))


dict1 = {'name':'章三','age':17}
print(dict1)
print(id(dict1))
dict1['name'] = 'asda'
print(dict1)
print(id(dict1))