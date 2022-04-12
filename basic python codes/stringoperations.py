x = "hello world"
print(x.upper())
print(x.lower())
print(x.split())

""" formatting the string using .format() method """

print("Hello iam new and learning {}".format("python"))
print("I am {1} , I will eleminate the {0}".format("eren" , "enemy"))
print("Hello iam {p} I was this code authors favorite character".format(p="Naruto" , q= "Itachi" , r = "Eren"))

""" formatting the float using .format() method """

result = 14564/545
print("the result of the above division is {r:1.5f}".format(r = result))

""" formatting the string using fstring method """

name = "Naruto"
age = "30"
print(f"Hello my friend name is {name} and he is {age} years old")

