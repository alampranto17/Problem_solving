import random


def createBoard(n=8):
  m=[]
  for i in range(n):
    c=[]
    for j in range(n):
      c.append(0)
    m.append(c)
  for col in range(n):
      row = random.randint(0,n-1)
  return m
def printBoard(m):
  for i in range(len(m)):
    print(m[i])
  print()

def placeQueen(b):
    for i in range(len(b[0])):
        row=random.randint(0,(len(b[0])-1))
        b[row][i]=1
    return b




b=createBoard()
b=placeQueen(b)
printBoard(b)

def generateChromosome(n):
    chro=""
    for i in range(n):
        gene=random.randint(0,n-1)
        chro+=str(gene)
    return chro

def find_attack(chromosome):
    n=len(chromosome)
    attack=0
    for i in range(n):
        for j in range(i+1,n):
            if chromosome[i]==chromosome[j]:
                attack+=1
            elif abs(int(chromosome[i])-int(chromosome[j]))  == abs(i-j) :
                attack=1
    return attack


c=generateChromosome(8)
print(c)

print(find_attack(c))



