#Import time module
import time

def countdown(n):
    if n == 0 :
        print("BLAST OFF!!!!")
    else:
        print(n)
        print('*'*n)
        time.sleep(1)
        countdown(n-1)

a = int(input("enter the limit: "))
countdown(a)      