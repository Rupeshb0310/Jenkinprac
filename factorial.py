import sys
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)

def div(n):
    res=10/n
    return res

def main(n):
    res = fact(n)
    print(res)

if __name__ =='__main__':
    
    main(int(sys.argv[1]))