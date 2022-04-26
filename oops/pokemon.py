class Pokemon :
    def __init__(self , name , color , power , owner):
        self.name = name 
        self.color = color 
        self.power = power
        self.owner = owner
    def __str__(self):
        return("{0} , {1} , {2} , {3}").format(self.name , self.power, self.color , self.owner)

    def __color__(self , other):
        if(self.color == "grey" ):
            return self
        else:
            return other
        
p1 = Pokemon("pikachu", "yellow", 'thunder', 'ash ketchup')
p2 = Pokemon("golem", "grey", 'rock', 'harry')

print(p2.__color__(p1))