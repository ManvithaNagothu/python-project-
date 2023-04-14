def add(a,b,c,L):
    return int(L[a]) + int(L[b]) + int(L[c])

def append_nums(a,b,c,lst):
    lst.append(a)
    lst.append(b)
    lst.append(c)
    return lst
    
def check_list(alist, mylst, lst,count): 
    if len(alist) == 3:
        if (add(0,1,2,alist) == 10) or (add(0,1,2,alist) == 20) or (add(0,1,2,alist) == 30):
            count += 3
            append_nums(alist[0],alist[1],alist[2],lst)
            x = mylst.index(alist)
            
            for j in range(3):
                mylst[x].pop(0)
            return 
    elif len(alist) > 3:
        if (add(0,1,-1,alist) == 10) or (add(0,1,-1,alist) == 20) or (add(0,1,-1,alist) == 30):
            count += 3
            append_nums(alist[0],alist[1],alist[-1],lst)
            x = mylst.index(alist)
            mylst[x].pop(0)
            mylst[x].pop(0)
            mylst[x].pop(-1)
            return 
              
        elif (add(0,-2,-1,alist) == 10) or (add(0,-2,-1,alist) == 20) or (add(0,-2,-1,alist) == 30):
            count += 3
            append_nums(alist[0],alist[-2],alist[-1],lst)
            x = mylst.index(alist)
            mylst[x].pop(0)
            mylst[x].pop(-2)
            mylst[x].pop(-1)
            return 
        
        elif (add(-3,-2,-1,alist) == 10) or (add(-3,-2,-1,alist) == 20) or (add(-3,-2,-1,alist) == 30):
            count += 3
            append_nums(alist[-3],alist[-2],alist[-1],lst)
            x = mylst.index(alist)
            mylst[x].pop(-3)
            mylst[x].pop(-2)
            mylst[x].pop(-1)
            return
        else:
            return
    else:
        return
                
lst = list(map(int, input("Enter 52 values: ").split()))
mylst = [[] for i in range(7)]
count = 0

index = 0
while True:
    if lst == []:
        t = index
        break
    ele = lst.pop(0)
    i = index%7
    index += 1
    mylst[i].append(ele)
    check_list(mylst[i], mylst, lst,count)
    if mylst[i] == []:
        mylst[i].clear()
    
if lst == []:
    if t == count:
        print("Win:",t)
    elif t % 7 == 6:

        print("Loss:",t)
    else:
        print("Draw:",t)



   

         
