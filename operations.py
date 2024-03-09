# operations.py

# Logical operations
## and
a = True
b = False
c = a and b
print(c)

## or
c = a or b
print(c)

## not
c = not a
print(c)

# Identity operations
## is
a = 10
b = 20
c = a is b
print(c)

## is not
c = a is not b
print(c)

# Membership operations
## in
my_list = [1, 2, 3]
c = 1 in my_list
print(c)

## not in
c = 4 not in my_list
print(c)

# Bitwise operations
## and
a = 10
b = 20
c = a & b
print(c)

## or
c = a | b
print(c)

## xor
c = a ^ b
print(c)

## not
c = ~a
print(c)

## left shift
c = a << 2
print(c)

## right shift
c = a >> 2
print(c)

# Arithmetic assignment operations
a = 10
a += 5
print(a)

a = 10
a -= 5
print(a)

a = 10
a *= 5
print(a)

a = 10
a /= 5
print(a)

a = 10
a %= 5
print(a)

a = 10
a **= 5
print(a)

a = 10
a //= 5
print(a)

# Bitwise assignment operations
a = 10
a &= 5
print(a)

a = 10
a |= 5
print(a)

a = 10
a ^= 5
print(a)

a = 10
a >>= 5
print(a)

a = 10
a <<= 5
print(a)

# Logical assignment operations
a = True
b = False
a &= b
print(a)

a = True
b = False
a |= b

a = True
b = False
a ^= b
print(a)

# Membership assignment operations
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

my_list = [1, 2, 3]
my_list.pop()
print(my_list)

my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# Identity assignment operations
a = 10
b = a
print(b)