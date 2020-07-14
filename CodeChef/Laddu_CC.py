t = int(input())
min_laddu = {
	'INDIAN': 200,
	'NON_INDIAN': 400
}
contest_laddu = {
	'CONTEST_WON': 300,
	'TOP_CONTRIBUTOR': 300,
	'BUG_FOUND': 0,
	'CONTEST_HOSTED': 50
}

for _ in range(t):
	a, o = map(str, input().split())
	a = int(a)
	n_laddus = 0

	for _ in range(a):
		this_activity = str(input())

		bonus = 0

		if this_activity.startswith('CONTEST_WON'):
			bonus = max(0, 20-(int(this_activity.split()[1])))
			this_activity = this_activity.split()[0]

		elif this_activity.startswith('BUG_FOUND'):
			bonus = int(this_activity.split()[1])
			this_activity = this_activity.split()[0]

		n_laddus += contest_laddu[this_activity] + bonus

	print(n_laddus//min_laddu[o])