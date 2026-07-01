#Write a program using only the data types from Day 6 to store a student's complete profile:
#name, roll number, marks (as list), pass/fail (bool), and address (as a dict with city and pincode).

#OPTION- 1
Day6 = ('Bhushan', 112, [10,20,30], True, {'CITY': 'Bangalore','Pincode': 560066 })
print(Day6)
print(len(Day6))
print(type(Day6)) # TYPE is TUPLE here
print('-------------------------')
print(Day6[0])
print(type(Day6[0]))
print('-------------------------')
print(Day6[1])
print(type(Day6[1]))
print('-------------------------')
print(Day6[2])
print(type(Day6[2]))
print('-------------------------')
print(Day6[3])
print(type(Day6[3]))
print('-------------------------')
print(Day6[4])
print(type(Day6[4]))
print('-------------------------')

#OPTION- 2
Day7 = {'Name':'Bhushan','Roll No': 112,'Marks': [10,20,30],'PASS/FAIL': True,'CITY': 'Bangalore','Pincode': 560066}
print(Day7)
print(len(Day7))
print(type(Day7)) # TYPE is dict here
print('-------------------------')
print(Day7['Name'])
print(type(Day7['Name']))
print('-------------------------')
print(Day7['Marks'])
print(type(Day7['Marks']))
print('-------------------------')
print(Day7['PASS/FAIL'])
print(type(Day7['PASS/FAIL']))
print('-------------------------')
print(Day7['CITY'])
print(type(Day7['CITY']))
print('-------------------------')
print(Day7['Pincode'])
print(type(Day7['Pincode']))
