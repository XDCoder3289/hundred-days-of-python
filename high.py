values = input('Please enter a set of values: ').split()
high = 0
for v in values:
    if int(v) > high:
        high = int(v)
print(high)
