class Triangle:
    def __init__(self,x,y,z):
        self.a = x
        self.b = y
        self.c = z
    def perimeter(self):
        return self.a + self.b + self.c

t1 = Triangle(3,4,5)
t2 = Triangle(9,9,9)
print('三角形t1的周长为：', t1.perimeter())
print('三角形t2的周长为：', t2.perimeter())
