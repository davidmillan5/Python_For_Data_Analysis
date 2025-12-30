# Enumerate

collection = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(collection):
    # do something with value
    print(f"{index}: {value}")

# sorted

unsorted_list = [10,40,50,2,3,45,3,1,4,8,19,20,35,15,0]
print(sorted(unsorted_list))

# zip

seq1 = ["foo", "bar", "baz"]

seq2 = ["one", "two", "three"]

zipped = zip(seq1, seq2)

print(list(zipped))

# reversed

reversed_list = list(reversed(range(11)))
print(reversed_list)