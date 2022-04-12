aha = int(input())

setPrime = False

if (aha) > 1 :
    for kalyanam in range(2 , aha):
        if aha % kalyanam == 0 :
            setPrime = True
            break
if setPrime:
    print("nahi bhai prime nahi hai ye")
else:
    print("prime number hai bsdk")