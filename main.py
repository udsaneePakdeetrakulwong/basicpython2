# import ทุกฟังก์ชัน
#import numbers


# import บางฟังก์ชัน
#from numbers import factorial
from numbers import *

# import some function with alias
from numbers import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

# print(factorial(5))

print(fa(5))
print(fi(100))
