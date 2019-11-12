my_table = []
def add(table, thing):
	if thing in table:
		return False
	else:
		table.append(thing)
		return True

def squish(arr, pos, maxSize):
	if pos+maxSize-1 >= len(arr):
		return arr

	new_arr = arr[0:pos]
	sq = sum(arr[pos:(pos+maxSize)])
	if sq > maxSize:
		return arr

	new_arr.append(sq)
	new_arr += arr[(pos+maxSize):]

	return new_arr

def stair(arr, index, sizes) -> None:
	new = []
	for i in range(len(arr)):
		if(add(my_table, squish(arr, i, sizes[index]))):
			new.append(squish(arr, i, sizes[index]))

	for i in new:
		stair(i, index, sizes)

	if index < len(sizes) - 1:
		stair(arr, index+1, sizes)

	return None

def stairs(n, index, sizes):
	gen = [1] * n
	stair(gen, index, sizes) # This generates all the posibilities with one size

print("Calculates all the possible ways up a set of stairs given the how many steps are taken at a time (e.g. [1, \'or\' 3])\nand how many stairs there actually are")
nr = int(input("Stairs: "))
x = []
print("Input how many steps at a time:")
while -1 not in x:
	x.append(int(input("-1 to exit: ")))
	print("Types of step:", x)
x.remove(-1)

sizes = x
stairs(nr, 0, sizes)
print(my_table)