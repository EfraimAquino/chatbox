# print ('Hello World')

x = 1.3
y = 'string'
z = -1

print(str(x))
x = str(x)
print(type(x))

x = input ('input number') #return value is string always

#conditionals
if type(x) == str:
    print(x, 'is string')
if isinstance (x, str):
    print(x, 'is string pero pwedeng child nung string data type')

#convention for printing variables (recommended)
print(f'{x} - {y} - {z:.2f}')
