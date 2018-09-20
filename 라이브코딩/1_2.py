def solution(paragraph):
	check = []
	x = paragraph.split()
	answer = len(x)
	for word in x:
		word = word.lower()
		if not(word in check):
			check.append(word)
	return len(check)

if __name__ == "__main__":
	print(solution("Blue bird blue bird lovely blue bird Do not sit on green bean"))
