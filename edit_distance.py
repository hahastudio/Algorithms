def edit_distance(str1, str2):
	"""Input: two strings str1, str2
Output: Edit distance between these two strings.
	"""
	m = len(str1)
	n = len(str2)
	diff = lambda c1, c2: 0 if c1 == c2 else 1
	E = [[0] * (n + 1) for i in xrange(m + 1)]
	for i in xrange(m + 1):
		E[i][0] = i
	for j in xrange(1, n + 1):
		E[0][j] = j
	for i in xrange(1, m + 1):
		for j in xrange(1, n + 1):
			E[i][j] = min(E[i-1][j] + 1, E[i][j-1] + 1, E[i-1][j-1] + diff(str1[i-1], str2[j-1]))
	return E[m][n]

if __name__ == '__main__':
	s = "EXPONENTIAL"
	t = "POLYNOMIAL"
	print edit_distance(s, t)