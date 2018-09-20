def higher_than_average(L):
	answer = []
	average = 0
	for person in L:
		average += person['score']
	average = average / len(L)
	for person in L:
		if person['score'] > average:
			answer.append(person)
	sortedanswer = []
	while (len(answer) > 0):
		minidx = 0
		for i in range(len(answer)):
			if (answer[minidx]['score'] > answer[i]['score']):
				minidx = i
		sortedanswer.append(answer[minidx])
		del answer[minidx]
	return sortedanswer

def solution(x):
	answer = 0
	return answer

if __name__ == "__main__":
	x = [{"name": "Kim", "score": 50},
		{"name": "Yoon", "score": 60},
		{"name": "Lee", "score": 40}]
	print(higher_than_average(x))
