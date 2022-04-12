""" sets are the unique collection of elements in a array or a string """

myset = ["hello" , "iam" , "a " , "set" , "hello"]
set(myset)
print(set(myset))
print(set("mississippi"))
s1 = {1 , 2 , 2 , 3 , 4 , 4 , 5}
s2 = {5 , 6 ,  8 , 9 , 6}
print(s1)
print(s1-s2)
print(s1 | s2 )
print(s1 ^ s2)