# list use [...]
number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jany', 'Wasan']
mixed = [10, 25.75, True, 'Nee']

# Access to the list
print(number[1])
print(name[3])
print(name)
print(mixed[2], mixed[3])

# Get length
print("สมาชิกทั้งหมดของ number = ", len(number))

# make empty list
data = []

# Append list
data.append(10)
data.append(15)
data.append(20)
print(data)

# update list
data[1] = 12
print(data)


for n in number:
    print(n)

# Summation
sum = 0
for num in number:
    sum += num

print(f"sum={sum}")
