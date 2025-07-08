#
# with open("Sample.txt",'w') as f:
#     f.write('Hello World')
#     i=0
#     while i<100:
#         f.write("Alam Pranto")
#         i=i+1
#
# with open("Sample.txt","r") as f:
#    while f.readline(100)!='':
#        print(f.readline(100))
#        f.readline(100)
#
#    print(f.tell())

#work with binary data
#
# with open("C:/Users/Alam Pranto/Pictures/Screenshots/Screenshot 2025-05-05 211830.png","rb") as f:
#     with open("sampleShot.png",'wb') as f1:
#         f1.write(f.read())

# work with json file
import json
# # l=[1,2,3,4,5]
# # with open("list.json",'w') as f:
# #     json.dump(l, f)
#
# with open("list.json","r") as f:
#     l=json.load(f)
#     print(l)
#

class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
    #
    # def __str__(self):
    #     return f"Name : {self.fname} {self.lname} Age : {self.age} Gender : {self.gender}"
    #
    # def format(self):
    #     return f"Name : {self.fname} {self.lname} Age : {self.age} Gender : {self.gender}"  # formation is most important
person=Person("Alam","Pranto",23,"Male")

# print(person)

def ShowingObject(person):
    if isinstance(person,Person):
        return {'name': person.fname +' '+ person.lname , 'Age': person.age ,'Gender' : person.gender }


with open("list.json",'w') as f:
    json.dump(person,f,default=ShowingObject,indent=4)

with open("list.json",'r') as f :
    print(type(json.load(f)))