s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4, 5, 6, 7}

union = s1 | s2  # union of set


print("s2 is superset of s1:", s2.issuperset(s1), s2 > s1)
print("S1 is subset of s2", s1.issubset(s2), s1 < s2)  # or by s2>s1
print("The Intersection of set is:", s1.intersection(s2))
print("The Union of set is: ", union)
print("Is DisJoint", s1.isdisjoint(s2))
print("set from list", set([1, 2, 2, 11, 1, 1, 3, 4, 5, 2]))
