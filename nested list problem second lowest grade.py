students = []  #creating an empty list to store the students' names and scores
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    students.sort(key=lambda x: x[1]) #sorting the list of students based on their scores in ascending order


dup=[]
f=0
for i in range(len(students)):
    for j in range(i+1,len(students)):
        if students[i][1] == students[j][1]: 
            dup.append(students[i])
            dup.append(students[j]) 
            f=1

print(dup)
if f==0:
    if len(students)==1:
        print(students[0][0])
    else:
        print(students[1][0]) #if there is only one student in the list of students:
    
else:
    second=0
    s1=[]
    dup.sort(key=lambda x:x[1])
    if students[0][1]<dup[0][1]:
        for i in range(len(dup)):
            if dup[0][1]==dup[i][1]:
                s1.append(dup[i][0])
        s1.sort()
        for i in range(len(s1)):
            print(s1[i])
    elif students[0][1]==dup[0][1]:
        for i in range(len(dup)):
            if dup[0][1]==dup[i][1]:
                s1.append(dup[i][0])
        s1.sort()
        for i in range(len(s1)):
            print(s1[i])