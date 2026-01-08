#3. WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
#Sample Input
#N = 5
#Scores= 2 3 6 6 5
#Sample output
#5
#Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is
#5. Hence, we print 5 as the runner-up score.
n=int(input("Entger the number of competitors:"))
a=[]
for i in range(0,n):
    c=int(input("Enter:"))
    a.append(c)
a.remove(max(a))
print("Score of runner up is:",max(a))