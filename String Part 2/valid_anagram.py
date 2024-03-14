#Accepted
def isAnagram(s, t):
    counter=0
    flag=False
    dict1={}
    dict2={}
    for i in s:
        if(dict1.__contains__(i)):
            dict1.update({i:dict1.get(i)+1})
        else:
            dict1[i]=1
    for i in t:
        if(dict2.__contains__(i)):
            dict2.update({i:dict2.get(i)+1})
        else:
            dict2[i]=1
    if(len(dict1)==len(dict2)):
        for i in dict1:
            if(dict1.get(i)==dict2.get(i)):
                counter=counter+1
            else:
                continue
        if(counter==len(dict1) and counter==len(dict2)):
            flag=True
        else:
            flag=False
    else:
        flag=False
    return flag
if __name__=="__main__":
    s=input("Enter 1st String: ")
    t=input("Enter 2nd String: ")
    t=t.casefold()
    s=s.casefold()
    resp=isAnagram(s,t)
    print(resp)