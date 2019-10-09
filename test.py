'''
Created on 2019/10/09

@author: t17cs050
'''
    
p = 0
while p < 10:
    if 6 < p < 10:
        print('p = ' , p)
        p += 1
    else:
        print('Not print')
        p += 1       

for x in {1, 2, 3}:
    print(x)

q = 0
while q < 5:
    if q % 2 == 0:
        for y in {'#', "+"}:
            print(y)
    q += 1
        
    
    