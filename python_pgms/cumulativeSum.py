#Given a list of n integers, 
# print a new list such that 
# every element in the new list represents the cumulative sum of all the elements until that position.

ls = [1,2,3,4,5]
sum=0

new_ls = []
for i in range(len(ls)):
    sum+=ls[i]
    new_ls.append(sum)

print(*new_ls)


