#Write a program that checks if the key 'email' exists in a dictionary. Print 'Found' if it does, else print 'Not found'.

Dic = {'Name': 'Bhushan', 'Age': 30, 'City': 'Mumbai', 'email': 'morebhushan.92@gmail.com'}
print(Dic)
print('=========================')
for i in Dic.keys():
    if(Dic[i] == Dic['email']):
        print('Found', Dic[i])
    else:
        print('Not Found')
