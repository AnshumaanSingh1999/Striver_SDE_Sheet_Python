#Accepted
def reversewords(s):
    a=[]
    a=s.split(' ')
    print(s)
    print(a)
    c=''
    i=len(a)-1
    while(i>=0):
        if(len(a[i])==0):
            i=i-1
            continue
        else:
            c=c+a[i]+" "
            i=i-1
    c=c.strip()
    return c
if __name__ == "__main__":
    s=input("Enter String")
    resp=reversewords(s)
    print(resp)