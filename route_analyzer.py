
input_valid = False
while input_valid == False:
	route = input('What route did you take today?')			#Asking for user input
	time = input('How long did it take you?')

	routes = []
	with open('route_data.txt' , 'r+') as data:				#getting routes already in text file
		raw = data.read()
		for line in raw.split('\n'):
			road = line.split(' ')[0]
			if road not in routes:
				routes.append(road)
			else:
				pass

		if route == '':										#if no route was entered, just continues to analyzing
			break

		if route in routes:
			data.write('\n' + route + ' - ' + time)
			input_valid = True
		elif route not in routes:							#if new route is entered, checks to make sure they meant to add a new route
			if input('Is this a new route? (Y/N)') == "Y":
				data.write('\n' + route + ' - ' + time)
				routes.append(route)
				input_valid = True
			else:
				pass
		else:
			input_valid = True

with open('route_data.txt' , 'r+') as data:					#updating data with new data added
	raw = data.read()

def average(route):											#takes list and gives an average in seconds for easy ordering
	total = 0
	for tm in route:
		totalSecs = 0
		parts = [int(s) for s in tm.split(':')]
		totalSecs = parts[0] * 60 + parts[1]
		total += totalSecs
	average = total / len(route)
	return int(average)

def time(sec):												#makes the times look nice
	minutes = int(sec / 60)
	sec = int(sec % 60)
	if len(str(sec)) == 1:
		sec = '0' + str(sec)
	return str(minutes) + ':' + str(sec)


averages = {}												#creates dictionary with routes and respective averages
for rt in routes:
	times = []
	for ln in raw.split('\n'):
		if ln.split(' ')[0] == rt:
			times.append(ln.split(' ')[2])
		else:
			pass
	averages[rt] = average(times)

quickest = sorted(averages, key=averages.__getitem__)		#sorts the routes by times

print('Average times from fastest to slowest:')

for x in quickest:
	print(x + ' : ' + time(averages[x]))