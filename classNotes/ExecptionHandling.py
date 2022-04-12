try : 
    mark1 = int(input("enter your marks in termend: "))
    mark2 = int(input("enter your marks in MIdterm: "))
    mark3 = int(input("enter your marks in Internals : "))
    totalPercentage = (mark1/50)*100 + (mark2/50)*100 + 40
except ValueError:
    print("please enter correct marks")
print(totalPercentage)


