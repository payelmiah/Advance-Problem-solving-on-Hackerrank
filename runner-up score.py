n=int(input())
l=list(map(int,input().split())) #taking input in list format on same line separated by space for array or list elements
l.sort()
l=list(dict.fromkeys(l)) #removing duplicates from list using dict.fromkeys() method which creates a dictionary with list elements as keys and then converting it back to list
print(l[-2])