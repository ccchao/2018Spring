import random
a = []
for i in range(100):
    a.append(random.randint(-500,500))

largest=0
second_largest=0
smallest=501
secondSmallest=501

for i in range(100):
    if a[i]>largest:
        second_largest = largest
        largest = a[i]
    elif a[i]>second_largest:
        second_largest = a[i]
    if a[i]<smallest:
        secondSmallest = smallest
        smallest = a[i]
    elif a[i]<secondSmallest:
        secondSmallest = a[i]

for p in range(99,0,-1):
    for q in range(p):
        if a[q] > a[q+1]:
            temp = a[q]
            a[q] = a[q+1]
            a[q+1] = temp

m = (a[49]+a[50])/2

print("The largest value in the list:", largest)
print("The smallest value in the list:", smallest)
print("The second-largest value in the list:", second_largest)
print("The second-smallest value in the list:", secondSmallest)
print("the median value of the elements in the list:", m)   
