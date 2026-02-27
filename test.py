if __name__ == '__main__':
    students = []  
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        students.sort(key=lambda x: x[1]) 

    dup=[]
    f=0
    from collections import Counter
    scores = [item[1] for item in students]
    score_count = Counter(scores)
    for item in students:            #rup = [item for item in students if score_count[item[1]] > 1]
        if score_count[item[1]] > 1:
            dup.append(item)
            f=1
    if f==0:
        if len(students)==1:
            print(students[0][0])
        else:
            print(students[1][0])
    else:
        second=0
        s1=[]
        if students[0][1]<dup[0][1] and students[1][1]==dup[0][1]:  #student<dup such as 1,3,3,5
            for i in range(len(dup)):
                if dup[0][1]==dup[i][1]: 
                    s1.append(dup[i][0])
            s1.sort()
            for i in range(len(s1)):
                print(s1[i])
        elif students[0][1]==dup[0][1]: #student=dup such as 1,1,3,5 or 1,1,3,3,5 or 1,3,3,3,5,6,6,6
            g=0
            n=0
            for i in range(len(dup)):
                if dup[0][1]<dup[i][1] and g==0:
                    s1.append(dup[i][0])
                    g=1

                    
                if g==1: 
                   if dup[i][1]==dup[i-1][1]:
                       s1.append(dup[i][0])
                       
                   else:
                        n+=1
                        if n==2:
                            break
                
            if g==0:
                l=0
                for i in range(len(students)):
                    if students[i][1]<students[i+1][1]:
                        s1.append(students[i+1][0])
                        l=1
                        break
                if l==0:
                    dup.sort(key=lambda x: x[0])
                    for i in dup:
                        print(i[0]) 
                else:
                    s1.sort()
                    for i in range(len(s1)):
                        print(s1[i])       
                
            else:
               s1.sort()
               for i in range(len(s1)):
                   print(s1[i])
        else:
            print(students[1][0])
