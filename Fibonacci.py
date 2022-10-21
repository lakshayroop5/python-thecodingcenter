def fib(n): #Nth FIBONACCI number generator function 
    if n==1 or n==2: #1st and 2nd terms are 1
        return 1
    else:
        return fib(n-1)+fib(n-2) #all other terms will be calculated recursively

n=int(input("Enter how many fibonacci terms you want to print: ")) #taking user input 
print("The fibonacci series upto ",n,"th term is:-") #giving desired output
for i in range(1,n+1):
    print(fib(i),end=" ") #looping till n terms and printing the terms as space seperated integers