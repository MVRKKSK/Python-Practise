class point:

    def __init__(self , x ,y):
        self .x = x
        self.y = y

    def move(self):
        print('move it')
    def draw(self):
        print("draw it")
point1 = point( 4 , 5)

print(point1.x)
