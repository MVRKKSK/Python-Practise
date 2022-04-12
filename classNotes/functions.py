def sample(i , s ="function"):
    s = "this is python class"
    print(s)

sample(5)

def count(i=5):
    if(i==0):
        return 0
    recursive = count(i/10)

    return recursive+1
    

print(count())