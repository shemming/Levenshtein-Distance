import sys
import time

def read_file(file_name):
	file1 = open(file_name, 'r')
	info = ""
	for line in file1:
		tmp = line.replace('\n', '')
		info = info + tmp
	file1.close()
	return info

start = time.time()

rows = read_file(sys.argv[1])
cols = read_file(sys.argv[2])

matrix = [[x for x in range(len(rows) + 1)] for x in range(len(cols) + 1)]
for x in range(len(matrix)):
	matrix[x][0] = x

edits = [[0 for x in range(len(rows) + 1)] for x in range(len(cols) + 1)]

for i in range(1, len(matrix[0])):
	for j in range(1, len(matrix)):
		if rows[i - 1] == cols[j - 1]:
			matrix[j][i] = matrix[j - 1][i - 1]
			edits[j][i] = 0
		else:
			x = matrix[j-1][i] + 1
			y = matrix[j][i-1] + 1
			z = matrix[j - 1][i-1] + 1

			if x < y and x < z:
				matrix[j][i] = x
				edits[j][i] = 1
			elif y < x and y < z:
				matrix[j][i] = y
				edits[j][i] = 2
			else:
				matrix[j][i] = z
				edits[j][i] = 0

edit_distance = matrix[len(matrix) - 1][len(matrix[0]) - 1]

s_result = ""
t_result = ""
i = len(edits) - 1
j = len(matrix[0]) - 1
while i != 0 and j != 0:
	if edits[i][j] == 0:
		s_result = rows[j - 1] + s_result
		t_result = cols[i - 1] + t_result
		i -= 1
		j -= 1
	elif edits[i][j] == 1:
		s_result = "-" + s_result
		t_result = cols[i-1] + t_result
		i -= 1
	elif edits[i][j] == 2:
		s_result = rows[j-1] + s_result
		t_result = "-" + t_result
		j -= 1
while j != 0:
	s_result = rows[j-1] + s_result
	j -= 1
while i != 0:
	t_result = cols[i-1] + t_result
	i -= 0

end = time.time()
elapsed_time = end - start


print("Input Sequences")
print("----------------------------")
print(rows)
print(cols)
print("----------------------------")
print("Aligned Sequences")
print("----------------------------")
print(s_result)
print(t_result)
print("----------------------------")
print("The minimum edit distance is", edit_distance)
print("Completed in", elapsed_time, "seconds.")








