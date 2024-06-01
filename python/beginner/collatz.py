## Program that prints out the number of steps that the evaluation of the Collatz conjecture takes for positive integers

def collatz(n):
    if n<1:
        print("Try a positive integer bigger or equal to 1.")
    elif n>=1:
        i=0
        while True:
            i+=1
            if n==1:
                break
            elif n%2 ==0:
                n = n/2
            elif n%2 ==1:
                n=3*n+1
        print(i)

collatz(19)
