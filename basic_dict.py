#This basic program contains different methods that can be used in dictionary

#create dictionary
my_dict = {}

#adding values
my_dict['id']=1
my_dict['name']="Nisha"
my_dict['state']="karnataka"

#printing dictionary
print(my_dict)

#length of dictionary
print(len(my_dict))

#fetching values
print(my_dict.values())
#fetching keys
print(my_dict.keys())
#fetching individual value with the help of key
print(my_dict['name'])

#printing values with the help of loop
for k,v in my_dict.items():
    #prints keys and values
    print(k,v)
    #prints only values
    print(v)
    #prints only keys
    print(k)

#deleting dictionary
# method1
del my_dict['state']
#method2
my_dict.pop('name')
print(my_dict)

#deleting entire dictionary
del my_dict