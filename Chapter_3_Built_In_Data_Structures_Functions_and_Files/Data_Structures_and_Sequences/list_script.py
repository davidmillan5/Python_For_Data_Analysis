a_list = [2, 3, 7, None]

tup = ("foo", "bar", "baz")

b_list = list(tup)

print(b_list)

b_list[1] = "peekaboo"

print(b_list)

gen = range(10)

print(list(gen))


# Adding and removing elements

b_list.append("dwarf")
print(b_list)

# Insert in a specific location
b_list.insert(1, "red")
print(b_list)

# Operation pop remove and returns an element at a particular index

print(b_list.pop(2))

print(b_list)

# Elements can be removed by value, using remove

b_list.append("foo")
b_list.remove("foo")
print(b_list)

print("dwarf" in b_list)

print("dwarf" not in b_list)

## Concatenating and combining lists

first_list = [4, None, "foo"]
second_list = [7, 8, (2, 3)]
third_list = first_list + second_list
print(third_list)

fourth_list = [[1, 2], [3, 4], [5, 6]]

# using the extent method

#third_list = first_list.extend(second_list)
#print(first_list.extend([4, None, "foo", 7, 8, (2, 3)]))

everything = []
for unit in fourth_list:
    everything.extend(unit)

print(everything)


# Sorting
a = [7, 2, 5, 1, 3]
a.sort()
print(a)

b = ["saw", "small", "He", "foxes", "six"]
b.sort(key=len)
print(b)


# Slicing

seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5])
seq[3:5] = [6,3]
print(seq)

print(seq[:5])

print(seq[3:])

print(seq[-4:])
print(seq[-6:-2])

print(seq[::2])
print(seq[::-1])


# Dictionary