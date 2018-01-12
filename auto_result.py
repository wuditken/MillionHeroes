import map_

def auto(question, option):
	scores = map_.map_options(question, option)
	result = [scores]
	for score_index in range(len(scores)):
		if scores[score_index] == max(scores):
			result.append(score_index+1)
			break
	return result