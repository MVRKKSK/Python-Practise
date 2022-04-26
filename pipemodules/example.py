from pipe import where , select

list1 = [ 1 , 2 , 3 , 4 , 5 , 6]

list2 = list(list1| where(lambda e : e%2 ==0)| select(lambda e : e*e))

print(list2)