score = int(input("Enter score: "))
if 90 <= score <= 100:
    print ("Your score is ", score, ", Grade is A")
elif 80 <= score < 90:
    print("Your score is", score, ", Grade is B")
elif 70 <= score < 80:
    print("Your score is", score, ", Grade is C")
else:
    print("Your score is ", score, ", Grade is F")
