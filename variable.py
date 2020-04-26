
a = 3
b = 4.92
c = "itgenius"
print(a)
print(b)
print(c)
print(a, b, c)

x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)

# boolean
status = True
msg = False

print(status, msg)


print("price per product", b, "baht")

# Method 1
print("ราคาขายต่อชิ้น  %f baht" % b)

# Method 2
print("ราคาขายต่อชิ้น  %.2f baht  มีจำนวน %d ชิ้น" % (b, a))

# Method 3
print(f"ราคาขายต่อชิ้น {b} baht มีจำนวน {a} ชิ้น")
