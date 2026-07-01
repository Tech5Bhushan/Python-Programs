#Add a new key 'city' to an existing dictionary and update the 'age' key to a new value. Print the full updated dictionary.

'''
various methods to add new keys to a dictionary in Python :
1. Using Assignment Operator (=)
2. Using update()
3. Using | Operator
'''

Dic = {'Name':'Bhushan', 'Age':18, 'Grade': 12}
print(Dic)

print("==============================================")
#1. Using Assignment Operator (=)'
print("==============================================")

Dic['City'] = 'Bangalore'
Dic['Age'] = 20
print(Dic)

print("==============================================")
#2. Using update()'
print("==============================================")

Dic.update({'City1':'Chennai'})
Dic['Age'] = 25
print(Dic)

print("==============================================")
#3. Using | Operator'
print("==============================================")

res = Dic | {'Age':30,'City2':'Mumbai'}

print(res)

print("==============================================")


