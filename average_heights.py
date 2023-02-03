heights = input("Enter the average student heights: ").split()
print(heights)
num = 0
i = 0
for h in heights:
    num += int(h)
    i += 1

average = num / i
print(round(average))
