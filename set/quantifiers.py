# for all
# all()
# return True if all the conditions are true

x = 4
conditions = {
    x > 3,
    x < 12,
    x == 4,
}
if all(conditions):  # instead of this x > 3 and x < 12 and x == 4
    print(True)

# There Exits
# any()
# return True if at least one of the conditions is true
x = 11
if any(conditions):  # instead of this x > 3 and x < 12 and x == 4
    print(True)


# we can use this to do something great
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cond = {(val < 10) for val in vals}
# now for all
print(all(cond))


def div_by_4(val):
    return val % 4


cond2 = {div_by_4(val) for val in vals}

print(any(cond2))
