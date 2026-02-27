if __name__ == '__main__':
    n=int(input())
    students_marks={} # creating an empty dictionary to store the students' names and scores
    for _ in range(n):
        name, *line = input().split() # taking input in the format of "name score1 score2 score3" which is called unpacking 
        scores =list(map(float, line)) # converting the scores from string to float using map() function and storing them in a list
        students_marks[name]=scores # adding the name and scores to the dictionary
    query_name = input()
    query_scores =students_marks[query_name] # retrieving the scores of the queried student from the dictionary
    average_score = sum(query_scores)/len(query_scores) # calculating the average score by summing the scores and dividing by the number of scores
    print("{:.2f}".format(average_score)) # printing the average score formatted to
