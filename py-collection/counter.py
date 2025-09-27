from collections import Counter

my_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = Counter(my_list)

print(counts)
# there is no key error in counter it is essentially a dictonery
# the dict implementation of this is here
dict = {}
for word in ["red", "green", "yellow", "red"]:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1


# counter is essentially doing the same thing but it is implemented in a sense that there is no key error


# we can you use counter to do this as well

for word in ["red", "green", "yellow", "red"]:
    counts[word] += 1


# also  if you search from in counter which it not present it will give its count zero instead of key error

print(counts["ukasha"])
print("The least common is :", counts.most_common()[-1][0])
