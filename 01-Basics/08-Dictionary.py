dict = {"Name" : 'Ravi', "Id" : 1001, "Salary" : 1000.00}
for i,j in dict.items():
    print("Key : {0}, Value : {1}".format(i,j))
    
    
dict2 = {"Address" : "Gzb"}
dict.update(dict2)
for i,j in dict.items():
    print("Key : {0}, Value : {1}".format(i,j))


#print(dictionary.keys())

#print(dictionary.values())


dict['Designation'] = 'Team Leader'

print(dict)

dict['Designation'] = 'Manager'

print('Updated')
print(dict)

del dict['Designation']
print(dict)
