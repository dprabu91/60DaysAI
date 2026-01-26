# Day 4 Loop

'''
#This is Just a sample code for loop in Python
for i in range(0, 10):
    print("Iteration:", i)


#This is Just a sample code for loop using list in Python

list = ['a','b',1,2]

for i in list:
    print("Element:", i)

    

#This is Just a sample code for loop using Dictionary in Python

dict = {'Name': 'Prabu', 'Age': 25 , "City" : "Dallas"}

for key, value in dict.items():
    print(f"{key}: {value}")
'''

key = ['Name', 'Age', 'City']
value = ['Prabu', 25, 'Dallas'] 

my_dict =dict(zip(key,value))

for k, v in my_dict.items():
    print(f"{k}: {v}")