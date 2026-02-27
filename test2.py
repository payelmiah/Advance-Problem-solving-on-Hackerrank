lst = []  
for _ in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name, score])
        
# Step 1: count scores
from collections import Counter

scores = [item[1] for item in lst]  # get all scores
score_count = Counter(scores)       # count how many times each score appears

# Step 2: filter students with duplicate scores
result = [item for item in lst if score_count[item[1]] > 1]

# Step 3: print result
for r in result:
    print(r)