numbers=int(input("Enter range:"))
print("list of Prime numbers till range is :",end=' ')
for n in range(1,numbers):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,end=' ')      