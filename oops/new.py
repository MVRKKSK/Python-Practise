class Point :
    def __init__(self , x =0 , y =0):
        self.x = x
        self.y = y

    def __str__(self):
        return("{0} , {1}").format(self.x , self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    def __division__(self , other):
        x = self.x / other.x
        y = self.y / other.y
        return Point(x,y)

    def __subtraction__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
    
    def __multiplication__(self , other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x,y)

p1 = Point( 1  , 4)
p2 = Point(4 ,5)
print(p1+p2)
print(p1.__subtraction__(p2))
