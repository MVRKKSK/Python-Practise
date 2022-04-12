""" mydict = {"hello":5 , "Iam" : 5 , "from" : 5 , "hyderabad" : 45}

n = input()
mydict4 = {}
print(mydict.get(n))
mydict4.update(n)
mydict.pop(n)
print(mydict4)

mydict2 = {"vitbhopal" : 5 , "hai": 6 , "bhopal": 5}
mydict3 = {**mydict , **mydict2}

print(mydict3)

print(mydic)
 """

""" d1 = {"naruto" : 9.5 , "aot" : 9.3 , "hxh" : 9.3 , "one piece" : 9.5}

n = int(input("enter your list length: "))

keys = []

for k in range(n):
    inputs= input()
    keys.append(inputs)


output = {k:d1[k] for k in keys}
print(output)
 """

greeting = "Hello"
def change_greeting(new_greeting):
    greeting = new_greeting
def greeting_world():
    world = "World"
    print(greeting, world)

change_greeting("Hi")
greeting_world()