# Ask for user input
userNum = input("Tell me a number. ")

#convert to float
userNum = float(userNum)

#do the computation
for multiple in range(2, 11):
	answer = userNum * multiple
	print("{} times {} is {}.".format(userNum, multiple, answer))