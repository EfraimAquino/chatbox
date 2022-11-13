#functions
def func (x, y, z):
    return x * y * z

test = func(3,4,5)
#print(test)

#class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return (self.length*2 + self.width*2)

rectangle = Rectangle (3,4)
print(rectangle.perimeter())