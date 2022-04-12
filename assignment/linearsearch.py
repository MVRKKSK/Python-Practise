linearSearch = []
n = int(input("enter no of elements: "))
for j in range(n):
    m = int(input("enter your list: "))
    linearSearch.append(m)
print(linearSearch)

k = int(input("enter your key to search in elements : "))
for i in linearSearch:
    if(k==i):
        print("your element is found in index" , i)