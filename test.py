if __name__ == '__main__':
    students = []  
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        students.sort(key=lambda x: x[1]) 

    dup=[]
    f=0
    for i in range(len(students)):
        for j in range(i+1,len(students)):
            if students[i][1] == students[j][1]:
                dup.append(students[i])
                dup.append(students[j]) 
                f=1
    if f==0:
        if len(students)==1:
            print(students[0][0])
        else:
            print(students[1][0])
    else:
        second=0
        s1=[]
        if students[0][1]<dup[0][1]:
            for i in range(len(dup)):
                if dup[0][1]==dup[i][1]:
                    s1.append(dup[i][0])
            s1.sort()
            for i in range(len(s1)):
                print(s1[i])
        elif students[0][1]==dup[0][1]:
            g=0
            for i in range(len(dup)):
                if dup[0][1]<dup[i][1] and g==0:
                    s1.append(dup[i][0])
                    g=1
                if g==1:  
                   if dup[i][1]==dup[i-1][1]:
                       s1.append(dup[i][0])
            s1.sort()
            for i in range(len(s1)):
                print(s1[i])
