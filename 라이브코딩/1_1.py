def solution(words):
	shortest = words[0]
	for i in range(0, len(words)):
		if len(words[i]) < len(shortest):
			shortest = words[i]
	return shortest

if __name__ == "__main__":
	print(solution(["Tiger", "cat", "lion", "mouse"]))
