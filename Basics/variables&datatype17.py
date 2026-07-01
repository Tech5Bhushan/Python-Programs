#Create a dictionary where the values are lists.
#Example: subject → list of marks. Print all the marks for one subject and find the highest mark.

Sub = {'ENGLISH': [20,30,40,50,60]}
print(Sub)
print(Sub['ENGLISH'])

for i in Sub['ENGLISH']:
    if(i > Sub['ENGLISH'][0]):
        TEMP = i

print(TEMP)