import map_sql

table = map_sql.get_villages()
for line in table:
	print (line	)

for r in range(1,20):

	temp = list(filter(lambda line: int(line[8]) <= r and int(line[8]) > 0 and line[4] == 'None', table))

	print ('__________________________________________________________________________________' + str(r))
	total = 0
	for line in temp:
		time = (line[8] * 20) /15
		# print (str(time) + '   '+ str(line[8]))
		total += line[8]*2
	print (str(total) + ' nr sate:' + str(len(temp)))

