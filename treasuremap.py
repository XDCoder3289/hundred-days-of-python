row1 = ['💀', '💀', '💀']
row2 = ['💀', '💀', '💀']
row3 = ['💀', '💀', '💀']

final = [row1, row2, row3]

print(f'{row1}\n {row2}\n {row3}')
print('')
print("This is the original table")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print("⬇")
print('')

num = input("Please enter where you want to place X: ")

sp = num.split(' ')
num1 = str(sp[0])

final[int(sp[0]) - 1][int(sp[1]) - 1] = 'x'
print(f'{row1}\n {row2}\n {row3}')
