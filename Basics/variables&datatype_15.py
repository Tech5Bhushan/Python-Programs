#Write a program that swaps the values of two variables without using a third variable.
Var1 = 5
Var2 = 10
print(Var1,Var2)
var1, var2 = Var2, Var1 #Python supports tuple unpacking for swaps: a, b = b, a
print(var1,var2)

print('========================')

Str1 = 'Bhushan'
Str2 = 'More'
print(Str1,Str2)
Str1 , Str2 = Str2 , Str1
print(Str1,Str2)