#Create a nested tuple: outer tuple holds two inner tuples — one with names of birds and one with names of big cats.
#Print the second element of the second inner tuple.

Tup = (('Parrot', 'Crow', 'Sparrow'),("BigCat1", "Bigcat2", "Bigcat3"))
print(type(Tup))
print(len(Tup))
print('============================')
print(Tup[0])
print(len(Tup[0]))
print('============================')
print(Tup[1])
print(len(Tup[1]))
print('============================')
print(Tup[1][1])
