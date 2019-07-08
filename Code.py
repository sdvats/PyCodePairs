print("Input the list of numbers seprated by space")
inputNumbers = input("Please Provide Input:").split(" ")
filteredList = []  # creating a empty list to store all filtered inputs
for x in inputNumbers:
    if(x.isdigit()):    # checking if the input is a digit or Not
        filteredList.append(int(x))   # Appending into filtered list

answerList = []
#Checking if the pairs have product even and Sum as Odd
for i in filteredList:   
    for j in filteredList:
        productofNumbers = i*j;    # Taking the product of pairs
        sumOfnumbers = i+j;        # Taking the sum of pairs
        if (productofNumbers % 2 == 0 and sumOfnumbers % 2 != 0):   # Checking the pairs with sum even and product odd with modulo operator
            pair = str(i) + ','+ str(j)  # making the pair
            answerList.append(pair)   # appending the pair in answer list
for each in answerList: 
    print('Pair with Product as Even and Sum as Odd:', each)  # printing the answer list
