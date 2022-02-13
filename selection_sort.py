list_to_range = input('Input list to range:')
list_to_range = [int(i) for i in list_to_range.split()]
l = len(list_to_range)

for i in range(l):
	el_pos = i
	for j in range(i, l):
		if list_to_range[el_pos] < list_to_range[j]:
			el_pos = j
	if i != el_pos:
		list_to_range[i], list_to_range[el_pos] = list_to_range[el_pos], list_to_range[i]

print(list_to_range)
