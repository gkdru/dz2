
def maxnumber():
    c = int(input())
    maxnum = 0
    while c != 0:
       if c > maxnum:
            maxnum = c
            c = int(input())
    print(maxnum)

maxnumber()


def srednumber():
    h = int(input())
    summa = 0
    dlina = 0
    while h != 0:
        summa=summa+h
        dlina=dlina+1
        h = int(input())
        b=summa/dlina
    print(b)

srednumber()
 
 
 
 

def reversenum(a1):
    
    if a1:
        print(a1%10,end="")
        reversenum(a1//10)


reversenum(a1 = int(input()))   
    
 