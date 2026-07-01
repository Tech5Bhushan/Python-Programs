#Create a list of 4 cities. Change the second city to a different one and print the updated list. Can you do the same with a tuple? Why?

Lst = ['Bangalore','Mumbai','Chennai','Assam']
print('Original List :',Lst)
Lst[1]= 'Pune'
print('Updated List :',Lst)
print('==================================================================')
Lst1 = ('Bangalore','Mumbai','Chennai','Assam')
print('Original List1 :',Lst1)
Lst1[1] = 'Pune'
print('Updated List1 :',Lst1)

#We can't update tuple, it will give "TypeError: 'tuple' object does not support item assignment"