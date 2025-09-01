

list1=[]
list2=[]

n=int (input("First matrix row: "))
m=int (input("First matrix colurm: "))
p=int (input("Second matrix row: "))
q=int (input("Second matrix colurm: "))

if(n==q):
    print("matrix multiplication possible")
else :
    print("matrix multiplication not possible")
    exit()



for i in range(0,n):
    listtemp=[]
    for j in range(0,m):
        listtemp.append(int(input("enter matrix value: ")))
    list1.append(listtemp)

for i in range(0,len(list1)):
    for j in range(0,len(list1[i])):
        print(list1[i][j],end=" ")
    print()


for i in range(0,p):
    listtemp=[]
    for j in range(0,q):
        listtemp.append(int(input("enter second matrix value: ")))
    list2.append(listtemp)

for i in range(0,len(list2)):
    for j in range(0,len(list2[i])):
        print(list2[i][j],end=" ")
    print()
final_list=[[0 for _ in range(n)] for _ in range(q)]

for i in range(n):
    for j in range(q):
        # for k in range(m):
        #     final_list[i][j]+=list1[i][k]+list2[k][j]
        final_list[i][j]=sum([list1[i][k]*list2[k][j] for k in range(m)])



for i in range(n):
    for j in range(q):
        print(final_list[i][j], end=" ")
    print()

