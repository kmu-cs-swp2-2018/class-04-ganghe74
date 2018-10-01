def bloodtype(data):
    result = {}

    for blood in data:
        if len(blood) == 3:
            if not 'AB' in result:
                result.update({'AB':1})
            else:
                result['AB'] += 1
        else:
            if not blood[0] in result:
                result.update({blood[0]:1})
            else:
                result[blood[0]] += 1
        if not blood[-1] in result:
            result.update({blood[-1]:1})
        else:
            result[blood[-1]] += 1

    return result

def solution(x):
    answer = 0
    return answer

if __name__ == '__main__':
	data = ['A+', 'B+', 'A-', 'O-', 'AB+', 'AB-']
	print(bloodtype(data))
