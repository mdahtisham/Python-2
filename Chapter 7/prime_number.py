num = int(input("Enter the number : "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        print("It is not prime")
        prime = True
        break
    else:
        print("It is prime")
        break