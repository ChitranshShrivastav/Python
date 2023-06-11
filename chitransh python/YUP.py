# TO print factorial of a no.
def r_fact(n):
    if n==1:
        return n
    else:
        return n*r_fact(n-1)
    num=int(input("enter the number: "))
    if num<0:
        print("no factorial exist: ")
    elif num==0:
        print("fact of 0 is 1.")
    else :
        print("the fact. of",num,"is",r_fact(n))