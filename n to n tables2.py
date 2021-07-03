#n to n tables
k,j,o=map(int,input().split())
for i in range(k,j+1):
    for j in range(1,o+1):
        print(i,'×',j,'=',i*j)
