# Display the number that appears exactly k times

ls = [1,6,3,3,4,4,5]
k = 2
n=len(ls)

d = {}

for i in range(0,n):
    
    if ls[i] in d.keys():
        d[ls[i]] += 1
    else:
        d[ls[i]] = 1
for a,b in d.items():
    if b==k:
        print(a)
