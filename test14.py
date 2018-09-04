answer = int(input("3 + 4 = "))
while answer != 7:
    print("Wrong Answer: ", answer)
    if answer == 0:
        break
    answer = int(input("3 + 4 = "))
else:
    print("Correct Answer: ", answer)
