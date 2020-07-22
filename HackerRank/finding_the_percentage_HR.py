n = int(input())
student_marks = {}

for _ in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores

query_name = input()

k = student_marks[query_name]

print('{:0.2f}'.format(sum(k)/len(k)))


