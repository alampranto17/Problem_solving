# Code here
arr=[3,2,1,2,1,4,5,8,6,7,4,2]

de={}
for i in range(len(arr)):
    de[arr[i]]=[]

for i in range(len(arr)):

   de[arr[i]].append(i)

finalvalue=0
for i in de:
    if(len(de[i])>1):
        maxvalue=de[i][-1]-de[i][0]
        print("maxvalue ",maxvalue)
        finalvalue=max(maxvalue,finalvalue)


print(finalvalue)

