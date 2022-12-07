def count_top_calorie_carriers(calorie_carriers):
	f = open("day_1_input.txt", "r")

	counted_calories = []
	current = 0
	for line in f:
		try:
			val = int(line)
			current = current + val
		except:
			counted_calories.append(current)
			current = 0
	f.close()

	return sum(sorted(counted_calories)[-calorie_carriers:])

print('Part 1')
print(count_top_calorie_carriers(1))

print('Part 2')
print(count_top_calorie_carriers(3))